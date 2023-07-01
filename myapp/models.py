from django.db import models

# Create your models here.
class User(models.Model):
    #クラス変数

    account_name = models.CharField(max_length=100, unique=True) #アカウント名
    password = models.CharField(max_length=100,default="password") #パスワード
    
    def __str__(self):
         return self.account_name
            
class Photo(models.Model):
    image = models.ImageField(upload_to="myapp/")


