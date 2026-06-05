from lxml import html
from request import *
import json

def parser(url):
    data = request(url)
    tree = html.fromstring(data)

    title=tree.xpath('string(//h1[@class="profile-title--bold"]/text())') or "N/A"
    address = tree.xpath("string(//li[contains(@class,'masthead-list__item--bold')]/following-sibling::li[1])") or "N/A"
    description=tree.xpath("string(//li[contains(@class,'masthead-list__item--bold')]/following-sibling::li[2])") or "N/A"
    reviews=tree.xpath('string(//b[@class="review-score hide-for-small"]/text())') or "N/A"
    review_count=tree.xpath('string(//span[@class="review-count"]/text())').replace("(", "").replace(")", "") or "N/A"
    about = tree.xpath("""
        normalize-space(
        string(
            //h2[contains(text(),'About our')]
            /following-sibling::div[@class='toggle-area__content'][1]
            //div[@class='truncate-text']
        )
    )
    """) or "N/A"

    office_details = {}

    office_section = tree.xpath(
        "//h2[contains(text(),'Office Details')]/following-sibling::div[contains(@class,'toggle-area__content')][1]"
    )

    if office_section:
        rows = office_section[0].xpath(".//div[contains(@class,'experience-section')]")

        for row in rows:
            label = row.xpath(
                "normalize-space(.//div[contains(@class,'experience-label')])"
            ).rstrip(":")

            value = row.xpath(
                "normalize-space(string(.//div[contains(@class,'experience-value')]))"
            )

            office_details[label] = value
    area_of_practices = tree.xpath(
        "//h2[contains(text(),'Areas of Practice')]"
        "/following-sibling::div[contains(@class,'toggle-area__content')][1]"
        "//ul[@id='aopList']/li/text()"
    )

    area_of_practices = [x.strip() for x in area_of_practices if x.strip()]
    
    output={
        "title":title,
        "address":address,
        "description":description,
        "reviews":reviews,
        "review_count":review_count,
        "about":about,
        "office_details":office_details,
        "area_of_practices":area_of_practices
    }
    with open("output.json",'w',encoding='utf-8') as f:
        json.dump(output,f,indent=4,ensure_ascii=False)
parser("https://www.martindale.com/organization/skoler-abbott-presser-pc-267867/springfield-massachusetts-692829-f/")
    