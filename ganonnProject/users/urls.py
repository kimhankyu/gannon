from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/',  views.loginView, name='login'),
    path('signup/', views.signupView, name='signup'),
    path('logout/', views.logoutView, name='logout'),
    path('mypage/', views.mypageView, name='mypage'),

]
