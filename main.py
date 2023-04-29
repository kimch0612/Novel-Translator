from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
import json
import urllib.request
import time

def translate():
    f = open("temp.txt", 'rt', encoding='UTF-8', errors='ignore')
    origin = f.read()
    origin_text = urllib.parse.quote(origin)
    data = "source=ja&target=ko&text=" + origin_text
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', client_id)
    request.add_header('X-Naver-Client-Secret', client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode == 200):
        response_body = response.read()
        result = response_body.decode("utf-8")
        out = json.loads(result)
        with open("output.txt", "a", encoding="utf-8") as f:
            f.write(out['message']['result']['translatedText'] + "\n\n\n\n")
    else:
        print("Error Code: " + rescode)
    
    os.remove('temp.txt')

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
                with open("temp.txt", "a", encoding="utf-8") as f:
                    f.write(epititle + "\n\n" + epibody + "\n\n\n\n")
                translate()
                driver.find_element_by_xpath('//*[@id="contentMain-readNextEpisode"]/span').click()
                time.sleep(10)
            except:
                break

with open('account.json', 'rt', encoding='UTF8') as json_file:
    json_data = json.load(json_file)
    client_id = json_data["ClientID"]
    client_secret = json_data["ClientSecret"]

init_chrome()
init_crawling()
crawler()
driver.close()