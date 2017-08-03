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

def loginSession(driver = None):
    if driver == None:
        print "driver is None"
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
    return driver

def statusParser(driver):
    statusHtml = driver.page_source
    soup = BeautifulSoup(statusHtml,"html.parser")
    #driver.save_screenshot('testing.png')
    #print soup.text
    light1_Powerstate = soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl01_label3").text
    light2_Powerstate = soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl02_label3").text
    light3_Powerstate = soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl03_label3").text
    light4_Powerstate = soup.find(id="ctl00_ContentPlaceHolder1_Repeater1_ctl04_label3").text
    '''
    allState = {
        "1" : light1_Powerstate,
        "2" : light2_Powerstate,
        "3" : light3_Powerstate,
        "4" : light4_Powerstate
    }
    '''
    def statusFormat(status):
        if status[1] == "f":
            return 0
        else:
            return 1
    statusList = [
                                          0,
            statusFormat(light1_Powerstate),
            statusFormat(light2_Powerstate),
            statusFormat(light3_Powerstate),
            statusFormat(light4_Powerstate)
            ]
    #allStateJson = json.dumps(allState)
    #print allStateJson
    print "statusParser finished"
    return {
            "statusList": statusList,
            "driver"    : driver
            }
# flask call this
def statusPull():
    driver = loginSession()
    statusList = statusParser(driver)["statusList"]
    return statusList

def pressSwitchButton(lightID,actionInt,driver=None):
    if driver == None:
        driver = loginSession()
    xpath = '//*[@id="ctl00_ContentPlaceHolder1_Repeater1_ctl0' + str(lightID) + '_tr"]'
    elementLightClickStep0 = driver.find_element_by_xpath(xpath)
    elementLightClickStep0.click()
    #driver.save_screenshot('testing.png')
    #actionInt is 0 or 1 int
    xpath = "//*[@id='ctl00_ContentPlaceHolder1_iBtn_Light_O" + ("n" if actionInt else "ff") + "']"
    print xpath
    elementLight1_1 = driver.find_element_by_xpath(xpath)
    elementLight1_1.click()
    #driver.save_screenshot('testing.png')
# flask call this
def switchLight(lightID,action):
    action = 0 if action[1] == "F" else 1
    driver = loginSession()
    statusParsed = statusParser(driver)
    status = statusParsed["statusList"][lightID]
    driver = statusParsed["driver"]
    if action != status:
        pressSwitchButton(lightID,action,driver)
