''' 把某个url的HTML页面下载到本地 '''
import requests

url = 'https://liqui.io/Market/Pairs'
proxies = {
    'http': 'socks5://127.0.0.1:9999',
    'https': 'socks5://127.0.0.1:9999'
}

headers = {
    # "cookie": "__cfduid=d337b09a0780ffb14209c776d9cfa9f391510729810; lang=en; RB_PCID=1512445850064462915; RB_GUID=29d30c69-bf03-4a78-96af-f813d50b00fd; cf_clearance=5701ef3b669efc826cf7cb34c4863cf8420d6e59-1512797575-14400; csrftoken=KKlyrETInzZPfM8djiyT83ISGAKwrK7LlApNi7P0o3H2fRxuJQIdnWSyMMXe66ek; RB_SSID=PsivPe3PnX; _ga=GA1.3.700018907.1512445473; _gid=GA1.3.1442835974.1512780087; AWSALB=weumr5u2fyqKY0F+mnmZUcL13tdmcNwVk4fNrJmssKGYwPsY9Uf4pEDSqmIPXqjKMJIodQskCANVxvb4UQ++zAe3vyWWk2UhTYxV7idX6RsclKEPiih3P7VadEVT",
    "referer": "https://coinone.co.kr/chart/?site=Coinone&unit_time=1D",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
    "x-newrelic-id": "UwIOUVNTGwEFUVZQAgMP",
    "x-requested-with": "XMLHttpRequest",
    "accept": "* / *",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh - CN, zh;q = 0.9"
}
resp = requests.get(url)
# resp = requests.get(url, headers=headers)
# resp = requests.get(url, proxies=proxies)

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)

print('end...')
