from django.db import models

# Create your models here.
class Cut(models.Model):
    ten = models.CharField(max_length=200)
    soluong = models.IntegerField()
    def __str__(self):
        return self.ten
    
class Userinfo(models.Model):
    username = models.CharField(max_length=200)
    roomnumber = models.IntegerField()
    
    class Meta:
        db_table = 'loginpage_userinfo'
        verbose_name = 'User Info Login'
    # def __str__(self):
    #     return self.username 