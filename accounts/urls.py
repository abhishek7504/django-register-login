from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.client_login,name='client_login'),
]