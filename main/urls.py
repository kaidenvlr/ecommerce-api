from django.urls import path

from main import views

urlpatterns = [

    # User
    path('login/', views.login, name='login'),

]
