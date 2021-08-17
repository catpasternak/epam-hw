import json

from task01_scraper import ApiClient

SP_500 = ApiClient().full_data


def write_top10_by_attr(attr, percentage=False, reverse=False, data=SP_500):
    """Creates JSON file containing top 10 companies according to given criteria:
    :param attr: company attribute to sort by
    :type attr: str
    :param percentage: set to True if parameter is represented as percentage in data
    :type percentage: Bool
    :param reverse: defines sorting order
    :type reverse: Bool
    :param data: companies data
    :type data: List[CompanyData]
    :rtype: None
    """
    if percentage:
        top10_obj = sorted(data, key=lambda x: get_attr(x, attr), reverse=reverse)[:10]
    else:
        top10_obj = sorted(
            data, key=lambda x: (x[attr] is None, x[attr]), reverse=reverse
        )[:10]
    top10 = [obj.__dict__ for obj in top10_obj]
    file_name = "top10_by_" + attr
    with open(file_name, "w") as file_result:
        json.dump(top10, file_result, indent=4)


def get_attr(elem, attr):
    """Converts company's attribute value to float. Applicable when it is percentage.
    Puts None values in the end of sorted sequence.
    """
    if elem[attr]:
        return float(elem[attr].strip("%"))
    return float("-inf")


if __name__ == "__main__":
    write_top10_by_attr("price", reverse=True)
    write_top10_by_attr("p_e")
    write_top10_by_attr("growth", percentage=True, reverse=True)
    write_top10_by_attr("poten_profit", percentage=True, reverse=True)
