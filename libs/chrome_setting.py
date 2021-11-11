import os
import random
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# TODO REFACTORING
UserAgent = [
    'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'
]

# TODO REFACTORING
def setWebDriver():
    # ua = UserAgent()
    # flag = True
    # while flag:
    #     userAgent = ua.google
    #     word_list = userAgent.split()           
    #     for word in word_list:
    #         if word.startswith('(Macintosh'):
    #             break
    #         if word.startswith('Chrome') and not (word.endswith('0')):
    #             flag = False

    # print(userAgent)
    index = random.randint(0,4)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920x1080')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument(f'user-agent={UserAgent[index]}')
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
