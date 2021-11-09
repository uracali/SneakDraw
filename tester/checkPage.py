from bs4 import BeautifulSoup

from libs.chrome_setting import setWebDriver, quitDriver

driver = setWebDriver()
driver.get("https://www.nike.com/kr/ko_kr/")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup.text)
quitDriver(driver)