from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', signup_page, name='signup'),
    path('register-user/', RegisterView.as_view(), name='register_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/login/', login_view, name='login_token'),
    path('order-details/', order_details, name='order_details'),
    path('create-parcel/', parcel_creation, name='create_parcel'),
    # path('allparcel/', ParcelListView.as_view(), name='get_allParcels'),
    path('order/<str:tracking_number>/', order_info, name='order_info'),
    path('allparcel/', allParcel, name='allParcel'),
    path('report-table/', report_table, name='report_table'),
    path('parcelCreation/', createParcel, name='parcel_creation'),
    path('update-parcel/<str:tracking_number>/', update_parcel_status, name='update_parcel_status'),
    path('update-parceldetails/<str:tracking_number>/', UpdateParcelAPIView.as_view(), name='update-parceldetails'),
]
