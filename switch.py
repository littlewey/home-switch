from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from bs4 import BeautifulSoup
from credential import *
from config import *
import json


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (userAgent)

driver = webdriver.PhantomJS(desired_capabilities=dcap, service_log_path=phantomjsLogPath)

driver.set_window_size(1024, 768)
driver.get(url_initial)
# login
elementUser = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtID"]')
elementUser.send_keys(user)
elementPSW = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtPW"]')
elementPSW.send_keys(password)
elementPSW.send_keys(Keys.ENTER)
time.sleep(1)
# got status
driver.get(url_status)

statusHtml = driver.page_source
soup = BeautifulSoup(statusHtml,"html.parser")

light1_Powerstate = soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl01_label3").text
light2_Powerstate = soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl02_label3").text
light3_Powerstate = soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl03_label3").text
light4_Powerstate = soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl04_label3").text

allState = {
    "1" : light1_Powerstate,
    "2" : light2_Powerstate,
    "3" : light3_Powerstate,
    "4" : light4_Powerstate
}

allStateJson = json.dumps(allState)

print allStateJson

elementLight1_0 = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Repeater1_ctl03_tr"]')

elementLight1_0.click()


driver.save_screenshot('testing.png')
elementLight1_1 = driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_iBtn_Light_On']")
elementLight1_1.click()

#driver.save_screenshot('testing.png')


driver.get(url_status)

elementLight1_0 = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Repeater1_ctl02_tr"]')

elementLight1_0.click()


#driver.save_screenshot('testing.png')
elementLight1_1 = driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_iBtn_Light_On']")
elementLight1_1.click()


