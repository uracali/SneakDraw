from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from libs.chrome_setting import setWebDriver, quitDriver


class Worksout:
    def __init__(self, id, password):
        self.driver = setWebDriver()
        self.id = id
        self.password = password

    def login(self):
        self.driver.get(
            'https://www.worksout-raffle.co.kr/'
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/header/button'))
        )

        self.driver.find_element_by_xpath(
            "//*[@id='root']/header/button").click()
        self.driver.find_element_by_id('email').send_keys(self.id)
        self.driver.find_element_by_id('pwd').send_keys(self.password)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="loginModal"]/div/div/div[1]/div[2]/button'))
        )
        self.driver.find_element_by_xpath(
            '//*[@id="loginModal"]/div/div/div[1]/div[2]/button').click()

    def findDraw(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/header/button[2]'))
        )

        href_list = []
        targets = self.driver.find_elements_by_xpath(
            '//*[@id="root"]/section/div/ul/li[*]/a')
        for i in range(len(targets)):
            if targets[i].text == "ENTER RAFFLE":
                href_list.append(targets[i].get_attribute("href"))
        self.href_list = href_list

    def raffle(self):
        for href in self.href_list:
            self.driver.get(href)
            self.driver.find_element_by_css_selector('span.dummy').click()
            self.driver.find_element_by_css_selector(
                'div.dropDownLabel').click()
            time.sleep(1)  # wait for select bar
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="raffleForm"]/div[2]/div[2]/ul/li[1]/span'))
            )
            size_list = self.driver.find_elements_by_xpath(
                '//*[@id="raffleForm"]/div[2]/div[2]/ul/li[*]/span')
            for size in size_list:
                print(size.text)
                if size.text == 'XL' or size.text == '270':
                    size.click()
                    self.driver.find_element_by_xpath(
                        '//*[@id="raffleForm"]/div[3]/button').click()
                    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
                    alert = self.driver.switch_to_alert()
                    alert.dismiss()

            return "RAFFLE_SUCCESS"

    def quitDriver(self):
        quitDriver(self.driver)
