from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def init_chrome():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument(r'user-data-dir=C:\nt')
    driver = webdriver.Chrome("c:/chromedriver.exe", options=chrome_options)
    driver.implicitly_wait(7)

def init_crawling():
    global site, url
    site = 0
    url = input("긁어오기 시작할 소설의 URL을 입력해주세요: ")
    if 'kakuyomu' in url: #카쿠요무
        site = 1
    elif 'syosetu' in url: #소설가가 되자
        site = 2

def crawler():
    if site == 1:
        driver.get(url)
        time.sleep(1.5)
        while True:
            try:
                epititle = driver.find_element_by_css_selector("#contentMain-header > p").text
                epibody = driver.find_element_by_css_selector("#contentMain-inner > div > div > div").text
                with open("source.txt", "a", encoding="utf-8") as f:
                    f.write(epititle + "\n\n" + epibody + "\n\n\n")
                driver.find_element_by_xpath("//*[@id="contentMain-readNextEpisode"]/span").click()
            except:
                break