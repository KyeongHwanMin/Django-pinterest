# Django - Pinterest

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
## 프로젝트 스크린샷
### 홈페이지

![homepage](https://user-images.githubusercontent.com/17818416/137146931-b9c5f43f-dc54-40d0-9dff-1a65058972e4.png)

### 로그인 페이지
![login](https://user-images.githubusercontent.com/17818416/137146953-fbab06e3-ce59-46b2-a59b-a3f424a38fb9.PNG)

### 회원가입 페이지
![회원가입](https://user-images.githubusercontent.com/17818416/137147263-48dddafe-f790-40cf-a8fe-783f655d774a.PNG)


