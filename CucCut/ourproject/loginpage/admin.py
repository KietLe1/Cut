from django.contrib import admin
from loginpage.models import Cut
from loginpage.models import Userinfo
# Register your models here.
admin.site.register(Cut)
#admin.site.register(Userinfo)
@admin.register(Userinfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username', 'roomnumber']
