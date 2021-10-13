from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        unique_together = ('user', 'project') #1개만 구독 할 수 있게 만듬듬
