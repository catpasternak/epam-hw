import json

from task01_scraper import ApiClient

SP_500 = ApiClient().full_data


def write_top10_by_attr(attr, percentage=False, reverse=False, data=SP_500):
    if percentage:
        top10_obj = sorted(
            data,
            key=lambda x: float("-inf")
            if get_attr(x, attr) is None
            else get_attr(x, attr),
            reverse=reverse,
        )[:10]
    else:
        top10_obj = sorted(
            data, key=lambda x: (x[attr] is None, x[attr]), reverse=reverse
        )[:10]
    top10 = [obj.__dict__ for obj in top10_obj]
    file_name = "top10_by_" + attr
    with open(file_name, "w") as file_result:
        json.dump(top10, file_result, indent=4)


def get_attr(elem, attr):
    if elem[attr]:
        return float(elem[attr].strip("%"))
    return None


write_top10_by_attr("price", reverse=True)
write_top10_by_attr("p_e")
write_top10_by_attr("growth", percentage=True, reverse=True)
write_top10_by_attr("poten_profit", percentage=True, reverse=True)
