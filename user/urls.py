from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout'),

    path('participate/', views.participate, name='participate'),
    path('register/login/', auth_view.LoginView.as_view(template_name='user/login.html')),
    path('participate/logout/', auth_view.LogoutView.as_view(template_name='user/logout.html')),
    path('contact/', views.contact, name='contact'),
    path('contact/logout/', auth_view.LogoutView.as_view(template_name='user/logout.html')),


    path('handlerequest/', views.handlerequest, name = 'handlerequest'),

]
