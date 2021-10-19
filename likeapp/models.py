from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record')

    class Meta:
        unique_together = ('user','article') # user 와 article 쌍이 1개만 존재하도록 설정
