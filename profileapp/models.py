from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)  # 이미지 저장 경로, 없어도 된다.
    nickname = models.CharField(max_length=20, unique=True, null=True)  # 닉네임은 유일해야함.
    message = models.CharField(max_length=100, null=True)
