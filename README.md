# webservice_for_INMS

</br>

## > 프로젝트 개요

- "Integrated Network Monitoring Service" 중 web service 파트의 기본 프레임 입니다.
- 수집할 장비정보를 사용자로부터 입력, 삭제, 수정할 수 있도록 하여 poller 파트에서 참고하여 수집할 데이터를 정립합니다.
- poller가 수집하여 기록한 정형/비정형 데이터에 대하여 grafana와 연동하여 시각화된 장비 정보를 비개발자 관점에서 사용할 수 있도록 표현합니다.

</br>

## > 프로젝트 실행 환경

- centos 7.9
- python 3.6.2
- grafana 7.5.3
- mariadb 10.2.43(mysql 15.1)
- elastic search 6.8.6(lucene 7.7.2)

</br>

## > dotenv

```py
# 문자열에 따옴표("")를 쓰지 않으셔도 됩니다.
# "=" 앞뒤로 띄어쓰기를 하는 경우 경우에 따라 적용되지 않을 수 있습니다.

FLASK_APP = app.py
FLASK_ENV = development

WEB_HOST = localhost
WEB_PORT = 5000
DEBUG    = True

DB_USER     =
DB_PASSWORD =
DB_HOST     =
DB_NAME     =
DB_PORT     =
```

</br>

## > 가상환경 세팅

- /ect/ 경로에 Repository clone 후 project root 경로에 venv를 생성합니다.

```py
python3 -m venv venv
```

- 가상환경을 실행합니다.

```py
. .venv/bin/activate
```

- 패키지를 설치합니다.

```py
pip install -r requirements.txt
```

</br>

## > 프로젝트 실행

- project root 경로에서 `flask run`
- browser 주소란에 다음 주소를 복사/붙여넣습니다.
  - http://localhost:5000/snmp_device/list_view

</br>

## > 시연

![Grafana-of-device-Chrome-2022-04-28-22-40-34](https://user-images.githubusercontent.com/89192083/165766320-040d8700-98c8-4e9f-a4e5-6d585946da14.gif)
