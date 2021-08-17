import asyncio
from dataclasses import dataclass

import aiohttp
import requests
from bs4 import BeautifulSoup

URL = "https://markets.businessinsider.com/index/components/s&p_500"
CBR_URL = "http://www.cbr.ru/scripts/XML_daily.asp"


@dataclass
class SP500Companies:
    """Dataclass to store a single company record."""

    code: str
    name: str
    price: float
    p_e: float
    growth: str
    poten_profit: str

    def __getitem__(self, item):
        return self.__dict__[item]

class SP500Scraper():

    URL = "https://markets.businessinsider.com/index/components/s&p_500"
    
    def __init__(self, url=URL, pages=11):
        self.url = url
        self.main_table_urls = [(url + "?p=" + str(page)) for page in range(1, pages + 1)]
        self.main_table_htmls = []
        self.comp_pages_htmls = []
        self.pages_data = []
        asyncio.run(self.main())

    async def get_page_html(self, session, url):
        async with session.get(url) as response:
            html = response.text()
#            if url in self.main_table_urls:
            self.main_table_htmls.append(html)
#            else:
#                self.comp_pages_htmls.append(html)
            return html

    @staticmethod
    async def make_soup(html):
        return BeautifulSoup(html, 'lxml')

    async def get_page_data(self, html):
        page_data = []
        page_soup = await make_soup(html)
        row_soups =  page_soup.find_all("tr")[1:]
        for row_soup in row_soups:
            ext = DataExtractor(row_soup)
            company_url = ext.get_company_url(self.url)
            price = ext.get_price()
            growth = ext.get_growth()
            page_data.append((company_url, price, growth))
        return page_data


    async def main(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in self.main_table_urls:
                task = asyncio.create_task(self.get_page_html(session, url))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
            return results
#            async for html in await asyncio.gather(*tasks):
#                soup = await self.make_soup(html)
#                page_data = await self.get_page_data
#                self.pages_data.append(page_data)

if __name__ == '__main__':
    scraper = SP500Scraper()
    print('Check scraper.main_table_htmls')

class SP500Parser():

    CBR_URL = "http://www.cbr.ru/scripts/XML_daily.asp"

    def __init__(self, html):
        self.html = html
        self.usd_rate = _get_exchange_rate()

    @staticmethod    
    def _get_exchange_rate(url=CBR_URL):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "xml")
        rate_usd = soup.find("Valute", ID="R01235").find("Value").text.strip()
        return float(rate_usd.replace(",", "."))



class ApiClient:
    """Fetches S&P500 data, creates list of all companies records in `full_data` attribute.
    Performs lazy evaluation. Returns single record with `get_company` method.
    """

    def __init__(self, url=URL):
        self.url = url
        self._main_table_soups = None
        self._comp_page_soups = None
        self._main_table_data = None
        self._comp_page_data = None
        self._full_data = None
        self.exchange_rate = self._get_exchange_rate()

    def _get_exchange_rate(self, url=CBR_URL):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "xml")
        rate_usd = soup.find("Valute", ID="R01235").find("Value").text.strip()
        return float(rate_usd.replace(",", "."))

    def get_company(self, comp_code):
        """Returns a company record when company code is passed."""
        for comp in self.full_data:
            if comp.code == comp_code:
                return comp

    async def _get_page_soup(self, session, url):
        async with session.get(url) as response:
            resp_html = await response.text()
            page_soup = BeautifulSoup(resp_html, "lxml")
        return page_soup

    async def _get_main_table_soups(self):
        urls = [(self.url + "?p=" + str(page)) for page in range(1, 12)]
        async with aiohttp.ClientSession() as session:
            tasks = [
                asyncio.create_task(self._get_page_soup(session, url)) for url in urls
            ]
            await asyncio.gather(*tasks)

    @property
    async def main_table_soups(self):
        if not self._main_table_soups:
            self._main_table_soups = self._get_main_table_soups()
        await self._main_table_soups

    async def _get_comp_page_soups(self):
        comp_urls = [tup[0] for tup in await self._parse_main_table()]
        async with aiohttp.ClientSession() as session:
            tasks = [
                asyncio.create_task(self._get_page_soup(session, url))
                for url in comp_urls
            ]
            self._comp_page_soups = await asyncio.gather(*tasks)

    @property
    def comp_page_soups(self):
        if not self._comp_page_soups:
            asyncio.run(self._get_comp_page_soups())
        return self._comp_page_soups

    async def _parse_main_table(self):
        main_table_data = []
        for page_soup in await self._get_main_table_soups():
            row_soups = page_soup.find_all("tr")[1:]
            for row_soup in row_soups:
                company_url = self._get_company_url(row_soup)
                price = self._get_price(row_soup)
                growth = self._get_growth(row_soup)
                main_table_data.append((company_url, price, growth))
        return main_table_data

    @property
    def main_table_data(self):
        if not self._main_table_data:
            self._main_table_data = self._parse_main_table()
        return self._main_table_data

    def _parse_comp_pages(self):
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
        if not self._comp_page_data:
            self._comp_page_data = self._parse_comp_pages()
        return self._comp_page_data

    @property
    def full_data(self):
        if not self._full_data:
            self._full_data = []
            for tup in zip(self.main_table_data, self.comp_page_data):
                record = CompanyData(
                    tup[1][1], tup[1][0], tup[0][1], tup[1][2], tup[0][2], tup[1][3]
                )
                self._full_data.append(record)
        return self._full_data

class DataExtractor():

    def __init__(self, soup):
        self.soup = soup

    def get_price(self):
        price_field = self.soup.find_all("td", class_="table__td")[1]
        price = price_field.text.strip().split("\r")[0]
        price_rub = float(price.replace(",", "")) * self.exchange_rate
        return round(price_rub, 2)

    def get_growth(self):
        growth_field = self.soup.find_all("td", class_="table__td")[7]
        growth = growth_field.find_all("span")[1]
        return growth.text.strip()

    def get_company_url(self, main_url):
        root_url = main_url[: main_url.find("/", 10)]
        relative_path = self.soup.find("a")["href"]
        return root_url + relative_path

    def get_name(self):
        name_elem = self.soup.find("span", class_="price-section__label")
        return name_elem.text.strip()

    def get_code(self):
        code_elem = self.soup.find("span", class_="price-section__category")
        return code_elem.find("span").text.split()[-1]

    def get_p_e(self):
        p_e = None
        data_field = self.soup.find_all("div", class_="snapshot__data-item")
        for elem in data_field:
            target_elem = elem.find("div", class_="snapshot__header")
            if "P/E Ratio" in target_elem.text:
                p_e = float(elem.text.split()[0].replace(",", ""))
                break
        return p_e

    def get_profit(self):
        low_52 = high_52 = None
        low_field = self.soup.find_all(
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


#if __name__ == '__main__':
#    client = ApiClient()
#    print(client.full_data[10])
