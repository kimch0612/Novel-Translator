# Novel-Translator

## 동작이 확인된 환경
##### Code-Server v4.11.0 (amd64 system)
##### Windows 11 22621.1555
##### Python 3.8.10
##### Selenium 3.10.0

## 동작 구조
##### source.txt 파일에서 원문 파일을 불러와 Papago API를 이용해 번역 데이터를 뽑아오고, 그 데이터를 output.txt 파일에 저장합니다.

## 사용 방법
##### 실행하기 전, account.json 파일을 생성한 뒤 json 문법에 맞게 ClientID와 ClientSecret의 값을 입력해줍니다.
##### ClientID와 ClientSecret는 Papago API를 이용하기 때문에 Naver Developers Open API 사이트에서 발급받으면 됩니다.
##### 이후 main.py를 실행하면 됩니다.

## 대응 사이트
##### 카쿠요무 (kakuyomu.jp)

## 앞으로 추가할 기능
##### 캐릭터 이름을 미리 한글로 치환해두는 기능 추가
##### 소설가가 되자 사이트 등에서 자동으로 source 파일을 Crawling 해오는 기능 추가
##### 파일 이름이 output이 아니라 소설의 이름이 되도록 설정
