import os
import gzip
import hashlib
from concurrent.futures import ThreadPoolExecutor
import sys
from curl_cffi import requests
from product_db import *


def save_gzip(html_text, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with gzip.open(file_path, "wt", encoding="utf-8") as f:
        f.write(html_text)


def get_firm_id(url):
    url = url.rstrip("/")

    parts = url.split("/")

    last_part = parts[-1]

    if last_part.endswith("-f"):
        return parts[-2].split("-")[-1]

    return last_part.split("-")[-1]


def fetch_address_page(id,address_url, save_directory):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"148.0.7778.179"',
        'sec-ch-ua-full-version-list': '"Chromium";v="148.0.7778.179", "Google Chrome";v="148.0.7778.179", "Not/A)Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"19.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
        'cookie': 'mdcgeo={%22country%22:%22IN%22%2C%22state%22:%22GJ%22}; AMCVS_5C64123F5245AF950A490D45%40AdobeOrg=1; BIGipServerwebvis-web=663818250.0.0000; _gid=GA1.2.1205324394.1780476250; _ga=GA1.1.458511340.1780476155; _hjSessionUser_386321=eyJpZCI6IjM5MjdlNDYzLTQ4MDEtNTk2NS04ODUzLTY0Zjg0ZTIwZTZjNSIsImNyZWF0ZWQiOjE3ODA0NzYyNTA0NjksImV4aXN0aW5nIjp0cnVlfQ==; _uetsid=640b37005f2811f1b698cfad4e9a8e6f; _uetvid=640ba7805f2811f1bf4e7d809b350e27; _pk_ref.7200.fb7a=%5B%22upper_button_8-15%22%2C%22%22%2C1780476251%2C%22%22%5D; _pk_id.7200.fb7a=e39c9008c5f65f17.1780476251.; _ibp=0:mpxtl7x0:53a50c81-cd69-4cfe-b8fd-3d407c344ae4; _ibs=0:mpxtl7x3:bb0468ac-b6f8-4cf3-9d70-a3ad033b6659; year=YnJvd3NlcklkPTE0MDczMDg3NTI=; hour=c2Vzc2lvbklkPTQ5NTAxOTU5MyZyZWZlckRvbWFpblNlbzRCPXd3dy5tYXJ0aW5kYWxlLmNvbQ==; searchSeed=678148874; radiusSearch=30; mdc-search-criteria=e2tleXdvcmQ6LGxpbWl0OjMwLHByYWN0aWNlQXJlYXM6ezc4MDpXb3JrZXJzIENvbXBlbnNhdGlvbn0sbG9jYXRpb25zOntBYmJldmlsbGUsIEFMOmNpOjFzdDoxY3U6MX0sY2l0eTpBYmJldmlsbGUsc3RhdGU6MSxjb3VudHJ5OjEsY2F0ZWdvcnk6cGVvcGxlfQ==; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jun+03+2026+14%3A32%3A40+GMT%2B0530+(India+Standard+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=3408f3d3-1535-4bfd-946e-fb30a80a5ec0&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.martindale.com%2Fmarketyourfirm%2F%3Futm_source%3Dmartindale%26utm_medium%3Dlink%26utm_campaign%3Dupper_button_8-15&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; _ga_HE50QBXY1Z=GS2.1.s1780476250$o1$g1$t1780477360$j60$l0$h0; launch=prod-mac; AMCV_5C64123F5245AF950A490D45%40AdobeOrg=179643557%7CMCIDTS%7C20608%7CMCMID%7C49728056045357985381140870985610208943%7CMCAAMLH-1781160927%7C6%7CMCAAMB-1781160927%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1780563327s%7CNONE%7CvVersion%7C5.5.0; s_vnc365=1812092127058%26vn%3D2; s_ivc=true; s_inv=79315; gpv_v22=https%3A%2F%2Fwww.martindale.com%2F; BIGipServerlgl-martindale-k8sw_24080_POOL=3532656650.4190.0000; s_sess=%20s_sq%3D%3B%20s_cc%3Dtrue%3B; cf_clearance=wKMWjePrsyEEFZrEgyFpsnbCGxLbgiMbKVSPr1T58PM-1780559485-1.2.1.1-oFbZB8SDIX5jzS.yhrYxwsWxyv25lBgmCmOgKVxSsSvrSUzOBbt2rLw4FjEqkYuC1kZStMG6EmzPK.QDoE_mWBmHcvlKJ25UKolbFE68c_TaiTYB9Bt5R9ukL5PT2sr2jXd_hGCK2zhT2dhTTp7Nf3sUZI8P8raMS35Wbbl8uQyO8R1qW7_L8S8U.R5ZCyUpOR0kaLJDMGsgQPzKp4u.8Nxf3pz44aJUe7Vv9f7pLJNgrIeHS2jhC.XxWlfiY7iuFJ0PlEwqLh7kLVWGA8MJy2E8nKu798OlQIUNmJagcxxH4qSQmuSC2hUIOUw3PGwh7hYyR6WGASDn1afJJFsVyBKi0CSSBc.DFlq.eRVmJjr6Hn41wbk4N8I9BGffBHKsYe.wE6y9JFcYYtssGoermjSmHmAMP_rfkv.BYrbG7.I; __cf_bm=2PlqBELxfK8baC4cwe1H6NTLa22lghdMPOyTDoc2HFk-1780559485.799255-1.0.1.1-sLBzVmg9SjSWOzGCvFqTC8rcFCD7iFncVmy4dDdpYsmpdGZ59zPxwhhvF5_GtW2YmD.6ZvCfV5D8WiX3vJLEOBliwezVlJaWeqg2jZGgZeWnZZB2gwY8qF0CH82iwD.X; laravel_session=eyJpdiI6Ik9zTzVpeDhFK0gwd1FnWGxEV2hZTmc9PSIsInZhbHVlIjoibXhkYzNHaUFuOU8rd0xhM3laZG9hSXdjU3VVaDBQc2NrN0lrU1hRZ2E2VUtSM2IrbDIwZWtRMXg0dXNpd1ZNTERDdGVUZTJ3VnY5TzNTSUNmZ0J1Z3B0c3FUVjdnSUEwMHhLbmkrWVNUL2dHQnRHSGdxaW44SDlSYTJWa1M2bXMiLCJtYWMiOiJiNGY5Zjk5ZmU1ZWYzMjhmOWVmNTdhY2JjYjU4MDM2NzZhMjNkMTc0MDMxZjU2MmYxYmQ4NjdjMmU4ZDgxYTBjIiwidGFnIjoiIn0%3D; gpv_v12=Martindale.com%3ADirectory%3AProfileView%3AFirmProfile%3Alaw%20offices%20of%20marc%20friedman; s_nr30=1780559562249-Repeat; s_tslv=1780559562253; stats=20260603235246089354C,20260603005331335753C,FIRM_PROFILE,20260603005331056063C,20260603235126307180C,FIRM_PROFILE; _ga_19ND86TN6P=GS2.1.s1780556131$o4$g1$t1780559567$j60$l0$h0; _ga_ZVZW1DXN1H=GS2.1.s1780556131$o4$g1$t1780559567$j60$l0$h1478464404; invoca_session=%7B%22ttl%22%3A%222026-07-04T07%3A53%3A38.646Z%22%2C%22session%22%3A%7B%22invoca_id%22%3A%22i-f19ffec2-d4bd-4993-f797-dbec42cbe4c5%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22rn%22%3Afalse%2C%22ba%22%3Atrue%2C%22br%22%3Atrue%7D%7D',
    }

    filename = (
        hashlib.sha256(address_url.encode("utf-8")).hexdigest()
        + ".html.gz"
    )

    file_path = os.path.join(save_directory, filename)

    if os.path.exists(file_path):
        print(f"Already Saved: {filename}")
        return

    response = requests.get(
        address_url,
        headers=headers,
        impersonate="chrome124"
    )

    print(
        f"STATUS={response.status_code} "
        f"SIZE={len(response.text)} "
        f"URL={address_url}"
    )

    if response.status_code != 200:
        print(f"Failed: {address_url}")
        return

    if len(response.text) < 500:
        print(
            f"Skipped (response too small): "
            f"{address_url}"
        )
        return

    save_gzip(response.text, file_path)
    update_firmlink_status(id)
    
    print(f"Saved: {file_path}")


def scrape_page(id, url, save_directory):
    firm_id = get_firm_id(url)

    address_url = (
        f"https://www.martindale.com/"
        f"organizations/{firm_id}/other-offices"
    )

    fetch_address_page(
        id,
        address_url,
        save_directory
    )


def process(item):
    id=item["id"]
    target_url = item["link"]

    try:
        print(f"\nScraping: {target_url}")

        scrape_page(
            id,
            target_url,
            save_directory
        )


    except Exception as e:
        print(
            f"Error handling URL "
            f"{target_url}: {e}"
        )


if __name__ == "__main__":

    start = int(sys.argv[1])
    end = int(sys.argv[2])

    save_directory = (
        r"C:\Users\manan.prajapati\Desktop\Practice"
        r"\all_page_save\martindale\address_pagesave"
    )

    all_firm_links = fetch_firmlinks_batch(
        start,
        end
    )

    print(
        f"Total Links: "
        f"{len(all_firm_links)}"
    )

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(
            process,
            all_firm_links
        )

    print(
        "\nAll address pages "
        "processed successfully!"
    )