from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name = "accountapp"

# 127.0.0.1:8000/account/hello_world == accountapp:hello_world"
urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),  # 라우터(주소),hello_world 함수, hello_world로 이름설정

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),  # 로그인 view는 템플릿 필요
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
]
