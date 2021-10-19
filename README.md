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
- Django model에 변경사항이 생겼을때 아래 명령어로 migration 파일을 생성
```sh
  - python manage.py makemigrations
  - python manage.py migrate
```
<br>

## 프로젝트 스크린샷
### 홈페이지
![homepage](https://user-images.githubusercontent.com/17818416/137148930-04bfda6a-b1cc-4a80-93ab-c4d73de2c734.png)
### 로그인 페이지
![login](https://user-images.githubusercontent.com/17818416/137148882-24afd5b6-c07f-49f0-a093-85043de5f97d.PNG)
### 회원가입 페이지
![회원가입](https://user-images.githubusercontent.com/17818416/137148841-7f34683d-c951-404d-9de1-52fe2bcb502a.PNG)
### 나의 페이지
![mypage](https://user-images.githubusercontent.com/17818416/137148820-ae630138-c3b0-41cd-ba42-8ee807d90d50.PNG)
### 좋아요 기능
![좋아요](https://user-images.githubusercontent.com/17818416/137888437-fe642a2e-ef68-424a-8ba1-77f4bb116da9.PNG)



