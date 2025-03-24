from django.urls import path
from . import views

urlpatterns = [
   path('', views.index_view, name='index'),
   path('create/shipment/', views.create_shipment_view, name='create_shipment'),
   path('user/profile/', views.user_profile_view, name='user_profile'),
   path('shipments/', views.shipments_view, name='shipments')
   # path('repair/create/', views.repair_create_view, name='repair_create')
]
