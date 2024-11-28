from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.orders, name='orders'),
    path('buy/', views.add_order, name='buy'),
    path('<int:order_id>/', views.orders_detail_view, name='order_detail'),
    path('<int:pk>/update', views.OrderUpdateView.as_view(), name='order_update'),
    path('<int:pk>/delete', views.OrderDeleteView.as_view(), name='order_delete'),
]
