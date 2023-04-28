import os
import sys
import json
import urllib.request

def translate():
    with open('account.json', 'rt', encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        client_id = json_data["ClientID"]
        client_secret = json_data["ClientSecret"]
    f = open("test.txt", 'rt', encoding='UTF-8', errors='ignore')
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