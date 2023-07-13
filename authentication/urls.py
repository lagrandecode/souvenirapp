from django.urls import path
from . import views



urlpatterns = [
    path('',views.SignupView.as_view()),
    path('verify/',views.VerifyView.as_view(),name='verify'),
<<<<<<< HEAD
    path('pages/',views.AdminLogin.as_view(),name='pages'),
=======
    path('interface/',views.Interface.as_view(),name='interface'),
>>>>>>> c831198af3a9a7043c4d942f06099bbb030d8db4
]