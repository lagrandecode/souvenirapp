
from django.urls import path
from . import views




urlpatterns = [
    path('',views.ProductView.as_view(),name='product'),
    path('<int:pk>/',views.ProductViewDetail.as_view(),name='detail'),
]