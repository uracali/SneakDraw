import os
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setWebDriver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920x1080')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--single-process')

    chrome_options.add_argument(
        '--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(
        '/home/ubuntu/uracali/chromedriver', chrome_options=chrome_options)

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    #     "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    driver.implicitly_wait(10)

    return driver


def quitDriver(driver):
    driver.quit()
