from django.urls import path

from main import views

urlpatterns = [

    # User
    path('login/', views.login, name='login'),
    path('register/', views.RegisterUserAPIView.as_view(), name='register'),
    path('change-password/', views.ChangeUserPasswordView.as_view(), name='change-password'),

]
