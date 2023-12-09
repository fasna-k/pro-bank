from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('login/',views.user_login,name='user_login'),
    path('register/',views.user_register,name='user_register'),
    path('',views.home,name='home'),
    path('logout/',views.user_logout, name='user_logout'),
    path('newpage/',views.new_page,name='new_page'),
]