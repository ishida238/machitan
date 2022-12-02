from django.urls import path
from . import views

app_name = 'hospital'
urlpatterns = [
    path('', views.IndexView.as_view(),name="index"),

    #path('signup/', views.signup_view, name='signup'),
    #path('login/', views.login_view, name='login'),
    #path('logout/', views.logout_view, name='logout'),
    #path('other/', views.other_view, name='other'),

    path('login-success/', views.LoginSuccessView.as_view(), name='login-success'),
    path('U_logout_check/', views.U_logout_checkView.as_view(), name='U_logout_check'),
]