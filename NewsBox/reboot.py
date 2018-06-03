from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

def rebootModem():
    driver = webdriver.Firefox()
    driver.get("http://192.168.0.1")

    user = driver.find_element_by_name("loginUsername")
    pw = driver.find_element_by_name("loginPassword")

    user.clear()
    pw.clear()

    user.send_keys("xxx")
    pw.send_keys("xxx")
    pw.send_keys(Keys.RETURN)

    driver.get("http://192.168.0.1/RgConfiguration.asp")

    reboot = driver.find_element_by_css_selector(".simpleTable > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(1) > input:nth-child(1)")
    reboot.click()
    time.sleep(1)

    Alert(driver).accept()
    time.sleep(1)
    driver.close()
