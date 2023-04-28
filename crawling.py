from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os, urllib.request

def init_chrome():
    mobile_emulation = { "deviceName": "iPhone X" }
    chrome_options = webdriver.ChromeOptions() 
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument(r'user-data-dir=C:\novelpia')
    driver = webdriver.Chrome("c:/chromedriver.exe", options=chrome_options)
    url = "https://novelpia.com/"
    driver.implicitly_wait(7)
    driver.get(url)
    
def crawler():
    pass