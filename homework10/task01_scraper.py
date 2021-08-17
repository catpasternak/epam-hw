import asyncio
from dataclasses import dataclass

import aiohttp
import requests
from bs4 import BeautifulSoup

URL = "https://markets.businessinsider.com/index/components/s&p_500"
CBR_URL = "http://www.cbr.ru/scripts/XML_daily.asp"


@dataclass
class CompanyData:
    """Dataclass to store a single company record.

    :param code: company NASDAQ code
    :param name: company full name
    :param price: company stock latest price in USD
    :param p_e: company P/E index
    :param growth: company stock price growth in 1 year, percentage
    :param poten_profit: potential profit (%) if stocks bought on 52 Week Low and sold on 52 Week High
    """

    code: str
    name: str
    price: float
    p_e: float
    growth: str
    poten_profit: str

    def __getitem__(self, item):
        return self.__dict__[item]


class ApiClient:
    """Fetches S&P500 data, creates list of all companies records in `full_data` attribute.
    Performs lazy evaluation. Returns single record with `get_company` method.

    :param url: main page of S&P500 table
    :type url: str
    """

    def __init__(self, url=URL):
        """Constructor method."""
        self.url = url
        self._main_table_soups = None
        self._comp_page_soups = None
        self._main_table_data = None
        self._comp_page_data = None
        self._full_data = None
        self.exchange_rate = self._get_exchange_rate()

    def _get_exchange_rate(self, url=CBR_URL):
        """Retrieves RUB/USD exchange rate.
        :param url: CBR official site, exchange rates xml page
        :type url: str
        :return: RUB/USD exchange rate
        :rtype: float
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "xml")
        rate_usd = soup.find("Valute", ID="R01235").find("Value").text.strip()
        return float(rate_usd.replace(",", "."))

    def get_company(self, comp_code):
        """Returns a company record when company code is passed.
        :param comp_code: company NASDAQ code
        :type copm_code: str
        :return: company name, code, price, P/E, growth and potential profit
        :rtype: :class:`CompanyData`
        """
        for comp in self.full_data:
            if comp.code == comp_code:
                return comp

    async def _get_page_soup(self, session, url):
        """Returns Beautiful Soup object from page html retrieved from given url address."""
        async with session.get(url) as response:
            resp_html = await response.text()
            page_soup = BeautifulSoup(resp_html, "lxml")
        return page_soup

    async def _get_main_table_soups(self):
        """Returns awaitable object that contains Beautiful Soup objects created from all pages
        of main S&P500 table.
        """
        urls = [(self.url + "?p=" + str(page)) for page in range(1, 12)]
        async with aiohttp.ClientSession() as session:
            tasks = [
                asyncio.create_task(self._get_page_soup(session, url)) for url in urls
            ]
            self._main_table_soups = await asyncio.gather(*tasks)

    @property
    def main_table_soups(self):
        """Beautiful Soup objects created from all pages of main S&P500 table."""
        if not self._main_table_soups:
            asyncio.run(self._get_main_table_soups())
        return self._main_table_soups

    async def _get_comp_page_soups(self):
        """Returns awaitable object that contains Beautiful Soup objects created from all S&P500 companies
        individual pages.
        """
        comp_urls = [tup[0] for tup in self._parse_main_table()]
        async with aiohttp.ClientSession() as session:
            tasks = [
                asyncio.create_task(self._get_page_soup(session, url))
                for url in comp_urls
            ]
            self._comp_page_soups = await asyncio.gather(*tasks)

    @property
    def comp_page_soups(self):
        """Beautiful Soup objects created from all S&P500 companies individual pages."""
        if not self._comp_page_soups:
            asyncio.run(self._get_comp_page_soups())
        return self._comp_page_soups

    def _parse_main_table(self):
        """Returns part of S&P500 companies data available from main table.
        :return: List of tuples containing company individual page url, company price and growth
        :rtype: List[tuple]
        """
        main_table_data = []
        for page_soup in self.main_table_soups:
            row_soups = page_soup.find_all("tr")[1:]
            for row_soup in row_soups:
                company_url = self._get_company_url(row_soup)
                price = self._get_price(row_soup)
                growth = self._get_growth(row_soup)
                main_table_data.append((company_url, price, growth))
        return main_table_data

    @property
    def main_table_data(self):
        """Part of S&P500 companies data available from main table: company individual page url,
        company price and growth.
        :rtype: List[tuples]
        """
        if not self._main_table_data:
            self._main_table_data = self._parse_main_table()
        return self._main_table_data

    def _parse_comp_pages(self):
        """Returns part of S&P500 companies data available from companies individual pages.
        :return: List of tuples containing company name, code, P/E and potential profit
        :rtype: List[tuple]
        """
        comp_page_data = []
        for soup in self.comp_page_soups:
            name = self._get_name(soup)
            code = self._get_code(soup)
            p_e = self._get_p_e(soup)
            profit = self._get_profit(soup)
            comp_page_data.append((name, code, p_e, profit))
        return comp_page_data

    @property
    def comp_page_data(self):
        """Part of S&P500 companies data available from companies individual pages:
        company name, code, P/E and potential profit.
        """
        if not self._comp_page_data:
            self._comp_page_data = self._parse_comp_pages()
        return self._comp_page_data

    @property
    def full_data(self):
        """Returns all required data for each company from S&P500 organized as list
        of :class:`CompanyData` objects.
        :rtype: List[CompanyData]
        """
        if not self._full_data:
            self._full_data = []
            for tup in zip(self.main_table_data, self.comp_page_data):
                record = CompanyData(
                    tup[1][1], tup[1][0], tup[0][1], tup[1][2], tup[0][2], tup[1][3]
                )
                self._full_data.append(record)
        return self._full_data

    def _get_price(self, row_soup):
        """Gets company price from main table row.
        :param row_soup: Beautiful Soup object representing one company record from main table
        :type row_soup: :class:`BeautifulSoup`
        :rtype: float
        """
        price_field = row_soup.find_all("td", class_="table__td")[1]
        price = price_field.text.strip().split("\r")[0]
        price_rub = float(price.replace(",", "")) * self.exchange_rate
        return round(price_rub, 2)

    def _get_growth(self, row_soup):
        """Gets company growth from main table row.
        :param row_soup: Beautiful Soup object representing one company record from main table
        :type row_soup: :class:`BeautifulSoup`
        :rtype: str
        """
        growth_field = row_soup.find_all("td", class_="table__td")[7]
        growth = growth_field.find_all("span")[1]
        return growth.text.strip()

    def _get_company_url(self, row_soup):
        """Gets company individual page url from main table row.
        :param row_soup: Beautiful Soup object representing one company record from main table
        :type row_soup: :class:`BeautifulSoup`
        :rtype: str
        """
        root_url = self.url[: self.url.find("/", 10)]
        relative_path = row_soup.find("a")["href"]
        return root_url + relative_path

    def _get_name(self, soup):
        """Gets company name from company individual page.
        :param soup: Beautiful Soup object generated from company page
        :type soup: :class:`BeautifulSoup`
        :rtype: str
        """
        name_elem = soup.find("span", class_="price-section__label")
        return name_elem.text.strip()

    def _get_code(self, soup):
        """Gets company code from company individual page.
        :param soup: Beautiful Soup object generated from company page
        :type soup: :class:`BeautifulSoup`
        :rtype: str
        """
        code_elem = soup.find("span", class_="price-section__category")
        return code_elem.find("span").text.split()[-1]

    def _get_p_e(self, soup):
        """Gets company P/E index from company individual page.
        :param soup: Beautiful Soup object generated from company page
        :type soup: :class:`BeautifulSoup`
        :rtype: float, None
        """
        p_e = None
        data_field = soup.find_all("div", class_="snapshot__data-item")
        for elem in data_field:
            target_elem = elem.find("div", class_="snapshot__header")
            if "P/E Ratio" in target_elem.text:
                p_e = float(elem.text.split()[0].replace(",", ""))
                break
        return p_e

    def _get_profit(self, soup):
        """Gets company potential profit from company individual page.
        :param soup: Beautiful Soup object generated from company page
        :type soup: :class:`BeautifulSoup`
        :rtype: float, None
        """
        low_52 = high_52 = None
        low_field = soup.find_all(
            "div", class_="snapshot__data-item snapshot__data-item--small"
        )
        for elem in low_field:
            target_elem = elem.find("div", class_="snapshot__header")
            if "52 Week Low" in target_elem.text:
                low_52 = float(elem.text.split()[0].replace(",", ""))
                break
        high_field = soup.find_all(
            "div",
            class_="snapshot__data-item snapshot__data-item--small snapshot__data-item--right",
        )
        for elem in high_field:
            target_elem = elem.find("div", class_="snapshot__header")
            if "52 Week High" in target_elem.text:
                high_52 = float(elem.text.split()[0].replace(",", ""))
                break
        if not (low_52 and high_52):
            return None
        profit = high_52 / low_52 - 1
        return "{:.2%}".format(profit)
