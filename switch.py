from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from bs4 import BeautifulSoup
from credential import *

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (X11; CrOS x86_64 9460.73.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.134 Safari/537.36")

driver = webdriver.PhantomJS(desired_capabilities=dcap)

driver.set_window_size(1024, 768)
driver.get('http://www.puxiangdao.cn/Resident/')


elementUser = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtID"]')
elementUser.send_keys(user)

elementPSW = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtPW"]')
elementPSW.send_keys(password)


elementPSW.send_keys(Keys.ENTER)

time.sleep(1)

driver.get('http://www.puxiangdao.cn/Resident/My_Home/HomeControl.aspx')

statusHtml = driver.page_source
soup = BeautifulSoup(statusHtml,"html.parser")


light1=soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl01_label3").text
light2=soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl02_label3").text
light3=soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl03_label3").text
light4=soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl04_label3").text



elementLight1_0 = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Repeater1_ctl03_tr"]')

elementLight1_0.click()


elementLight1_1 = driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_iBtn_Light_On']")
elementLight1_1.click()

#driver.save_screenshot('testing.png')

