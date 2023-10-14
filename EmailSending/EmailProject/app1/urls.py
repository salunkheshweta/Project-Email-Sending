from django.urls import path
from . import views

urlpatterns =[
    path('sv/', views.signup_view)
]