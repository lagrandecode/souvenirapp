from django.urls import path
from . import views



urlpatterns = [
    path('',views.SignupView.as_view()),
    path('verify/',views.VerifyView.as_view(),name='verify'),
]