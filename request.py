from curl_cffi import requests as re

def request(url):
    payload = {}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.martindale.com/',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"148.0.7778.217"',
    'sec-ch-ua-full-version-list': '"Chromium";v="148.0.7778.217", "Google Chrome";v="148.0.7778.217", "Not/A)Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'Cookie': 'launch=prod-mac; mdcgeo={%22country%22:%22IN%22%2C%22state%22:%22GJ%22}; AMCVS_5C64123F5245AF950A490D45%40AdobeOrg=1; AMCV_5C64123F5245AF950A490D45%40AdobeOrg=179643557%7CMCIDTS%7C20608%7CMCMID%7C24371211224756744202422989225405759498%7CMCAAMLH-1781081843%7C12%7CMCAAMB-1781081843%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1780484243s%7CNONE%7CvVersion%7C5.5.0; s_vnc365=1812013043476%26vn%3D1; s_ivc=true; s_inv=0; year=YnJvd3NlcklkPTE4MTM3MzkyMTM=; hour=c2Vzc2lvbklkPTE2NTU1MzA3OTYmcmVmZXJEb21haW5TZW80Qj13d3cubWFydGluZGFsZS5jb20=; _ga=GA1.1.121149449.1780477045; invoca_session=%7B%22ttl%22%3A%222026-07-03T08%3A58%3A54.616Z%22%2C%22session%22%3A%7B%22invoca_id%22%3A%22i-c296a0f6-72a2-468e-966e-2555e1b1a7b1%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22rn%22%3Afalse%7D%7D; laravel_session=eyJpdiI6IkxQZmE2dEsxNTd2c1Mxc24xQXhIaVE9PSIsInZhbHVlIjoidEdpcG11VzZvaUEwekRpNUhoOTd0b25EN05EbDNucGp6cmJCWHRtNXk0RHlpRG5ETVhBeXlBUTgrOXZzQkpVZnRScmRLNU1FbXB1YnZENmpONzFzRVhKQkNLY2xTWU5LdGJjVUxnN1ZIb00xbVNXWERKcnpuVElLSFdaTDltVTMiLCJtYWMiOiI5ZTQyYjJmMTYyOGFlOGU4YTI5ZWNiMzQ2YzFkN2ExZmI1OWNkOGRkYzJiYWY5YzUzNjI4NGE3MzEwOTU3OTkxIiwidGFnIjoiIn0%3D; cf_clearance=USsfAgS6d19j8tzVqExZdxvnNgvloknzenMK7gMlYSo-1780477902-1.2.1.1-2HKKijVPBaYwNvbZ5iOT3zQq.s.xqqy5uytnaVO56ZSwarJ2cJHFCvFiX83pJLqMAhKMwLscwcs_iLTk_toQqheZ4mAdG70TnfV2Ba7q7Yt.cfcKzlgiWZGloAUZcAprAGWYpteegLnl_b6N4LCbHgmfgRAPo4Le4.M_wGL6HjI0DWukwUzJefKSjqyp3achHY2Pvqrl4FOMNqBDKGlWGeI2ygXKffMP3Bxg5_ACoo19rYYkvYgZX4ftws8dHZ.NIwIIP9ztY7v9aUnWQPlqz_615OtKaX2fSATF3UxYG8X2TQyPafuYFBTRZ6w4hwQqXkyuTfH9QD6jkQRU.zSiuagICTdZyN0BqXxVBWj0312EgHl6diQICTt16q257qnLJdvDXgC0HBVjILJoCYPlmgfNDlRJ3rWICfNaM1b9jO4; __cf_bm=aGGLiUn0qduTUg4A0I6kxQ0pDBumsG1krPe.6DmSGWA-1780477902.7608855-1.0.1.1-B6mDTLaXKCZ59z3zRe7dzr_RAXQTeemWh1AeHTJ48FBFHKUYgKz1nVaH0vei5MJ_X9z7UXCOlO1vvyc1dOZ5uaxLbll6cccn7LjEmA2Xgy5VIDwtZVUWwgBWroskYBl7; s_nr30=1780477902961-New; s_tslv=1780477902962; gpv_v12=Martindale.com%3AHomepage%3Aexplore%20the%20richest%20database%20of%20legal%20professionals; gpv_v22=https%3A%2F%2Fwww.martindale.com%2F; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3Dfindlawmartindale%25252Cfindlaw-global-v1%253D%252526c.%252526a.%252526activitymap.%252526page%25253DMartindale.com%2525253AHomepage%2525253Aexplore%25252520the%25252520richest%25252520database%25252520of%25252520legal%25252520professionals%252526link%25253DWorkers%25252520Compensation%252526region%25253DBODY%252526pageIDType%25253D1%252526.activitymap%252526.a%252526.c%252526pid%25253DMartindale.com%2525253AHomepage%2525253Aexplore%25252520the%25252520richest%25252520database%25252520of%25252520legal%25252520professionals%252526pidt%25253D1%252526oid%25253Dhttps%2525253A%2525252F%2525252Fwww.martindale.com%2525252Fareas-of-law%2525252Fworkers-compensation-lawyers%2525252F%252526ot%25253DA%3B; stats=20260603011149247877C,,BBAP,,20260603005738693284C,FIRM_PROFILE; _ga_19ND86TN6P=GS2.1.s1780477045$o1$g1$t1780477909$j53$l0$h0; _ga_ZVZW1DXN1H=GS2.1.s1780477045$o1$g1$t1780477909$j53$l0$h2007597054; laravel_session=eyJpdiI6IitiNnRNbTVGZGc0UkRRR09IYXlxOWc9PSIsInZhbHVlIjoidXdTZEk0TTZQeFR3NlFPUldVeFdNeXZzYkVZZ2ZwMGtKTEpENTRRVGZ3dEVnWmJ4eC8zaFlUUjNrdlFlSmVwUng0Z1hYS1RjalNCcUZFZG1yV0Rtc1NuUlVoMFhkWThuMU1JaE8xY2JPbmMzWjZtQWU3cTRJck56SzlIZiszVVUiLCJtYWMiOiJjNmZkZjkyNDYzZTIzYzkwY2NjMjMyZThiMTAzN2VkOWM5MjljM2I0M2Q2YWJmMDVkMTllNjZhZTAzZGNiNDM0IiwidGFnIjoiIn0%3D'
    }
    response = re.request("GET", url, headers=headers, data=payload, impersonate='chrome136')
    if response.status_code == 200:
        return response.text
    else:
        return None