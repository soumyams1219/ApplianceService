from django.urls import path,include
from . import views
from .views import *
app_name = 'guest'
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login_view,name='login'),
    path('verify-otp',views.verify_otp,name='verify-otp'),
    path('register',views.register,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('user/',include('user.urls')),
    path('administrator/',include('administrator.urls')),
    path('role-creation',RoleCreationAPIView.as_view(),name='role-creation'),
    path('role-list',RoleListAPIView.as_view(),name='role-list'),
    path('role/<int:pk>/',RoleRetrieveAPIView.as_view(),name='role-retrieve'),
]