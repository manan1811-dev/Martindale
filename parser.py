from request import *
from lxml import html
import os


def add_page_save_state(page, category_name):
    folder_path = r"C:\Users\manan.prajapati\Desktop\Practice\all_page_save\martindale\state"

    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(
        folder_path,
        f"{category_name}.html.gz"
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(page)


def add_page_save_city(page, category_name, state_name):
    folder_path = os.path.join(
        r"C:\Users\manan.prajapati\Desktop\Practice\all_page_save\martindale\city",
        category_name,
        state_name
    )

    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(
        folder_path,
        "page.html.gz"
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(page)


def state_parser(url):
    data = request(url)

    tree = html.fromstring(data)

    state_urls = tree.xpath(
        '//h2[contains(normalize-space(), "Browse by States")]/following-sibling::ul//a/@href'
    )

    state_names = tree.xpath(
        '//h2[contains(normalize-space(), "Browse by States")]/following-sibling::ul//a/text()'
    )

    category_name = url.rstrip("/").split("/")[-1]

    add_page_save_state(data, category_name)

    print(f"States Found: {len(state_urls)}")

    return state_urls, state_names, category_name


def city_parser(url, category_name, state_name):
    data = request(url)

    tree = html.fromstring(data)

    city_urls = tree.xpath(
        "//h3[@class='hide-for-small-only all-aop__initial']/following-sibling::ul[1]//a/@href"
    )

    city_names = tree.xpath(
        "//h3[@class='hide-for-small-only all-aop__initial']/following-sibling::ul[1]//a/text()"
    )

    add_page_save_city(
        data,
        category_name,
        state_name
    )

    print(f"Cities Found: {len(city_urls)}")

    return city_urls, city_names