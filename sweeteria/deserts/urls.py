from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.catalog, name='catalog'),
    path('add_candy/', views.add_candy, name='add_candy'),
    path('candy/<int:candy_id>/', views.candy_detail_view, name='candy_detail'),
    path('candy/<int:pk>/update', views.CandyUpdateView.as_view(), name='candy_update'),
    path('candy/<int:pk>/delete', views.CandyDeleteView.as_view(), name='candy_delete'),
]
