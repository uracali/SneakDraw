from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from pytz import timezone


class Nike:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=self.options, executable_path=r'./chromedriver')
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
                                    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

    def findDraw(self):
        self.driver.implicitly_wait(3)

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
            draw = targets_name[i].text
            print(draw)

            if date == today:
                if 'THE DRAW' in draw:
                    href_list.append(targets_href[i].get_attribute('href'))
            else:
                break

        return href_list

    def login(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(
            'https://www.nike.com/kr/launch/?type=upcoming&activeDate=date-filter:AFTER_DATE'
        )

        self.driver.find_element_by_xpath(
            '//*[@id="jq_m_right_click"]/div/ul/li[2]/a').click()
        self.driver.find_element_by_id('j_username').send_keys(self.id)
        self.driver.find_element_by_id('j_password').send_keys(self.password)
        self.driver.find_element_by_xpath(
            '//*[@id="common-modal"]/div/div/div/div/div[2]/div/div[2]/div/button').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="jq_m_right_click"]/div/ul/li[1]/div/div/label/span'))
        )

    def raffle(self, raffleList):
        for i in range(len(raffleList)):
            self.driver.get(raffleList[i])
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_xpath(
                '//*[@id="checkTerms"]/label/i').click()
            self.driver.find_element_by_class_name(
                'select-head'
            ).click()
            self.driver.find_element_by_css_selector(
                "li.list > a[data-value='46']"
            ).click()
            self.driver.find_element_by_xpath(
                '//*[@id="btn-buy"]'
            ).click()
            WebDriverWait(self.criver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     ' //*[@id="draw-entryTrue-modal"]/div/div/div/div[3]/p/button')
                )
            )
            self.driver.find_element_by_xpath(
                ' //*[@id="draw-entryTrue-modal"]/div/div/div/div[3]/p/button')
            return "RAFFLE_SUCCESS"

    def quitDriver(self):
        self.driver.quit()

    def test(self):
        self.driver.get(
            'https://www.nike.com/kr/launch/t/adult-unisex/fw/action-outdoor/CZ2239-600/hcmd90/nike-sb-dunk-low-pro-qs'
        )
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath(
            '//*[@id="checkTerms"]/label/i').click()
        self.driver.find_element_by_class_name(
            'select-head'
        ).click()
        self.driver.find_element_by_css_selector(
            "li.list > a[data-value='270']"
        ).click()
        self.driver.find_element_by_xpath(
            '//*[@id="btn-buy"]'
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                    ' //*[@id="draw-entryTrue-modal"]/div/div/div/div[3]/p/button')
            )
        )
        self.driver.find_element_by_xpath(
            ' //*[@id="draw-entryTrue-modal"]/div/div/div/div[3]/p/button')
        return "RAFFLE_SUCCESS"


if __name__ == "__main__":
    nike = Nike('8109h@naver.com', '15881144Sk!')
    nike.login()
    nike.test()
