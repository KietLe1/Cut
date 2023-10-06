from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login.as_view(template_name='index.html'), name='login'),
    
]