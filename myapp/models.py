from django.db import models
class login(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    rpassword=models.CharField(max_length=10)
  