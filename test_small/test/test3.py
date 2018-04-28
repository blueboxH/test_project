from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
url = 'https://kknews.cc/entertainment/b4qqxym.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
}

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = headers['User-Agent']

# driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=[
#                              '--ignore-ssl-errors=true'])
driver = webdriver.Edge()
driver.maximize_window()
driver.get(url)
driver.save_screenshot('01.png')
