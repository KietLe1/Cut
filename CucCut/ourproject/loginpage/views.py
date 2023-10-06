from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import Userinfo


class login(View):
    template_name = None
    def get(self, request):
        return render(request,self.template_name)
    def post(self,request):
        os = request.GET.get('OS', 'https://netnam.vn')
        username = request.POST.get('username', '').strip()
        roomnumber = request.POST.get('roomnumber', '').strip()
        filter = Userinfo.objects.filter(username=username,roomnumber=roomnumber)
        if filter.exists():
            return redirect(os)
        else:
            query = Userinfo.objects.create(username=username,roomnumber=roomnumber)
            query.save()
            return redirect(os)
# Create your views here.

        