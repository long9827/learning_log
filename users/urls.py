"""定义users的URL模式"""

from django.urls import path
from django.contrib.auth.views import login

from . import views

app_name = 'users'
urlpatterns = [
	#登录页面
	path('login/', login, {'template_name': 'users/login.html'}, name='login'),
	
	#注册页面
	path('register/', views.register, name='register'),
	
	#注销
	path('logout/', views.logout_view, name='logout'),
]
