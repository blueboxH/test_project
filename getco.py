import requests
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def has_form(driver, p):
    try:
        a = driver.find_element_by_class_name('form')
        print('{} >>>>>>>>>>'.format(p), a)
    except:
        print("{}can't find form!".format(p))
        if p == 'end':
            print(driver.page_source)

url = 'https://liqui.io/Market/Pairs'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
}

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = headers['User-Agent']

driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])
driver.maximize_window()
driver.get(url)
wait = WebDriverWait(driver, 10)
has_form(driver, 'before a')
a = wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'form')))
has_form(driver, 'behind a')
coo = driver.get_cookies()
cookies = {item['name']: item['value'] for item in coo}
print('cookies:->>>', cookies)
has_form(driver, 'end')

driver.quit()


resp = requests.get(url, cookies=cookies, headers=headers)
try:
    resp.raise_for_status()
    print('succeed!')
    print({str(v['Id']): v['Name'] for v in data})
except:
    print('failed')
url2 = "https://liqui.io/chart/history?symbol=1&resolution=1m&from=1513145032&to=1513749832"
res = requests.get(url2, cookies=cookies, headers=headers)
res.raise_for_status()
print(res.json())


