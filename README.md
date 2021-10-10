# Django

Python의 대표 웹 프레임워크 django를 이용해 Pinterest 특유의 카드형 레이아웃 디자인을 본딴 웹서비스 구현

- django 개발 패턴
- docker를 통한 실제 서버 배포
- Pinterest 카드형 레이아웃 구현
- MagicGrid, Bootstrap, Google Font 등 외부소스 활용
- AWS 기반 서버 배포


## 기술스택
- Python 3.9.x
- Django 3.2.x

## 장고 설치
```sh
pip install django
```
## 서버실행
```sh
python manage.py runserver
```
## Django migration 
- Django model에 정보 변경이 생겼을때 아래 명령어로 migration 파일을 생성
```sh
  - python manage.py makemigrations
  - python manage.py migrate
```
