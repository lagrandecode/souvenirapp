
from django.urls import path
from . import views




urlpatterns = [
    path('',views.OrderView.as_view(),name='order'),
    path('<int:pk>/',views.OrderDetailView.as_view(),name='order_update'),
    path('status/<int:pk>/',views.StatusUpdateView.as_view(),name='status'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)