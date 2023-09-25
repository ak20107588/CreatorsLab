from django.contrib import admin
from django.urls import path,include
from .import views
from .import form

urlpatterns = [
    path('',form.home),
    path('signup',form.signup_detail),
    path('login_detail',form.login_detail),
    path('logout',form.logout),
    path('fileupload',views.fileupload),
    path('dashboard',views.dashboard),
    path('uploadfile',views.uploadfile)
]
