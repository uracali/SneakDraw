import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setWebDriver():
    env = os.environ.get("IS_LOCAL")
    print({env})
    if(env == 'true'):
        print("is local")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])

        chrome_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options)

    else:
        print("Is not local")
        chrome_options = Options()
        chrome_options.binary_location = "/opt/python/bin/headless-chromium"
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920x1080')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--single-process')

        chrome_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(
            '/opt/python/bin/chromedriver', chrome_options=chrome_options)

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    #     "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

    return driver
