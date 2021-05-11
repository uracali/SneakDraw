from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

import time

class Nike:
    def __init__(self, id, password):
        print("here we are")
        self.id = id
        self.password = password
        self.options = webdriver.ChromeOptions() 
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=self.options, executable_path=r'./chromedriver')
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
        

    def findDraw(self):
        self.driver.implicitly_wait(3)
        # WebDriverWait함수를 적용 불가 ! -> time.sleep으로 대체
        time.sleep(2)

        targets =self.driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/section/div[1]/div/ul/li[*]/div[1]/div/div/div/div/div[1]/h3')
        targets_name = self.driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/section/div[1]/div/ul/li[*]/div[1]/div/div/div/div/div[1]/h6')
        targets_date = self.driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/section/div[1]/div/ul/li[*]")
        targets_href = self.driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/section/div[1]/div/ul/li[*]/div[1]/div/a")

        #오늘의 날짜
        today = datetime.today().strftime("%Y/%m/%d")
        # 오늘 응모에 참여해야하는 item url
        href_list = []
        
        for i in range(len(targets)):
            try:
                date = targets_date[i].get_attribute('data-active-date')[:10]
                draw = targets[i].text
                if date == today:
                
                    if '응모' in draw:
                        href_list.append(targets_href[i].get_attribute('href'))
                else:
                    break
                    
                
            except Exception as ex:
                print("Error Detected",ex)
                self.driver.quit()

        #url로 접속해 응모 클릭
        for i in range(len(href_list)):
            self.driver.get(href_list[i])
            wait = WebDriverWait(self.driver,10)
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[1]/section/div[2]/aside/div[2]/div[2]")))
                self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]/section/div[2]/aside/div[2]/div[2]").click()
                print("응모 성공")
            
            except Exception as ex:
                print("Error Detected")
                self.driver.quit()
        

    def login(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(
            'https://www.nike.com/kr/launch/?type=upcoming&activeDate=date-filter:AFTER_DATE'
        )

        self.driver.find_element_by_xpath('//*[@id="jq_m_right_click"]/div/ul/li[2]/a').click()
        self.driver.find_element_by_id('j_username').send_keys(self.id)
        self.driver.find_element_by_id('j_password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="common-modal"]/div/div/div/div/div[2]/div/div[2]/div/button').click()


    def findSizeInput(self):
        time.sleep(2)
        # 사이즈 찾기
        self.driver.find_element_by_xpath('/html/body/section/section/section/article/article[2]/div/div[4]/div/div[2]/form/div[1]/div[2]/div[1]/div/span[8]').click()

        time.sleep(0.5)
        # 바로 구매 버튼 클릭
        self.driver.find_element_by_xpath('//*[@id="btn-buy"]').click()


    def order(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath('// *[ @ id = "btn-next"]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="payment-review"]/div[1]/ul/li[2]/form/div/span').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('// *[ @ id = "payment-review"] / div[1] / ul / li[1] / div / div[1] / h6').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="payment-review"]/div[1]/ul/li[2]/form/div/span/label/span').click()
        time.sleep(3)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="complete_checkout"]').click()


        # 결제
        iframe = self.driver.find_element_by_xpath("/html/body/div[13]/iframe[2]")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/li[2]/a').click()
        self.driver.find_element_by_id('userPhone').send_keys('01056741111')
    
    def quitDriver(self):
        self.driver.quit()


if __name__ == '__main__':
    id = ""
    password= ""
    test = Nike(id,password)
    test.login()
    test.findDraw()
    test.quitDriver()
    






