from django.db import models

class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)