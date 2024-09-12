from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('api/login/', login_view, name='login_token'),
    path('order-details/', order_details, name='order_details'),
    path('create-parcel/', parcel_creation, name='create_parcel'),


]
