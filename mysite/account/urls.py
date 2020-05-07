from django.conf.urls import url,include
from account import views

app_name = 'account'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'registation/',views.registation,name='registation'),
    url(r'loginpage/',views.loginpage,name='loginpage'),
    url(r'logout/',views.logoutuser,name='logout'),
    url(r'user/',views.userpage,name='user'),
    url(r'profile/',views.profile,name='profile'),
    
]
