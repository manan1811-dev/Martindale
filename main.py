from request import *
from parser import *
from db import *

create_database()
create_state_table()
create_city_url_table()

urls = [
    "https://www.martindale.com/areas-of-law/workers-compensation-lawyers/",
    "https://www.martindale.com/areas-of-law/social-security-disability-lawyers/",
    "https://www.martindale.com/areas-of-law/medical-malpractice-lawyers/"
]

for category_url in urls:

    state_urls, state_names, category_name = state_parser(
        category_url
    )

    print(
        f"Category: {category_name} -> "
        f"{len(state_urls)} states found"
    )

    # Insert all states into DB
    insert_state_url(
        category_url,
        state_urls,
        state_names
    )

    for state_url, state_name in zip(
        state_urls,
        state_names
    ):

        city_urls, city_names = city_parser(
            state_url,
            category_name,
            state_name.strip()
        )

        if city_urls:

            insert_city_url(
                state_name.strip(),   # state_name
                state_url,            # state_url
                city_urls,            # city_urls
                city_names            # city_names
            )

            update_state_status(state_url)

        print(
            f"{state_name.strip()} -> "
            f"{len(city_urls)} cities found"
        )