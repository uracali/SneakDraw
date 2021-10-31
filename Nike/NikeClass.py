from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from pytz import timezone
from libs.chrome_setting import setWebDriver, quitDriver


class Nike:
    def __init__(self, id, password):
        self.driver = setWebDriver()
        self.id = id
        self.password = password

    def findDraw(self):
        targets = self.driver.find_elements_by_xpath(
            '/html/body/div[1]/div/div[1]/section/div[1]/div/ul/li[*]/div[1]/div/div/div/div/div[1]/h3')
        targets_name = self.driver.find_elements_by_class_name(
            'available-date-component')
        targets_date = self.driver.find_elements_by_xpath(
            "/html/body/div[1]/div/div[1]/section/div[1]/div/ul/li[*]")
        targets_time = self.driver.find_elements_by_xpath(
            '/html/body/div[1]/div/div[1]/section/div[1]/div/ul/li[9]/div[1]/div/div/div/div/div[1]/h3')
        targets_href = self.driver.find_elements_by_xpath(
            "/html/body/div[1]/div/div[1]/section/div[1]/div/ul/li[*]/div[1]/div/a")

        today = datetime.now(timezone('Asia/Seoul')).strftime("%Y/%m/%d")
        href_list = []
        for i in range(len(targets)):
            date = targets_date[i].get_attribute('data-active-date')[:10]
            print(date)
            draw = targets_name[i].get_attribute('textContent')
            print(draw)

            if date == today:
                if 'THE DRAW' in draw:
                    href_list.append(targets_href[i].get_attribute('href'))
            else:
                break

        return href_list

    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(
                'https://www.nike.com/kr/launch/?type=upcoming&activeDate=date-filter:AFTER_DATE'
            )
            self.driver.find_element_by_xpath(
                '//*[@id="jq_m_right_click"]/div/ul/li[2]/a').click()
            print(1)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="j_username"]')
                )
            )
            self.driver.find_element_by_id('j_username').send_keys(self.id)
            self.driver.find_element_by_id(
                'j_password').send_keys(self.password)
            print(2)
            self.driver.find_element_by_xpath(
                '//*[@id="common-modal"]/div/div/div/div/div[2]/div/div[2]/div/button').click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="jq_m_right_click"]/div/ul/li[1]/div/div/label/span'))
            )
            print(3)
            return True
        except Exception as ex:
            print("Login Failed, ErrorCode = ", ex)
            return False

    def raffle(self, raffleList):
        for i in range(len(raffleList)):
            try:
                self.driver.get(raffleList[i])
                WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="checkTerms"]/label/i'))
                )
                self.driver.find_element_by_xpath(
                    '//*[@id="checkTerms"]/label/i').click()
                self.driver.find_element_by_class_name(
                    'select-head'
                ).click()
                self.driver.find_element_by_css_selector(
                    "li.list > a[data-value='270']"
                ).click()
                self.driver.find_element_by_class_name(
                    'btn-buy'
                ).click()
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH,
                        ' //*[@id="draw-entryTrue-modal"]/div/div/div/div[3]/p/button')
                    )
                )
                self.driver.find_element_by_xpath(
                    ' //*[@id="draw-entryTrue-modal"]/div/div/div/div[3]/p/button').click()
            except:
                pass
        return "RAFFLE_SUCCESS"

    def quitDriver(self):
        quitDriver(self.driver)
