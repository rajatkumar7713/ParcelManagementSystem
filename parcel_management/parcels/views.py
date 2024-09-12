from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
# Create your views here.

#login 
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
def login_page(request):
    return render(request, 'login.html')

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

def order_details(request):
    # Logic to fetch order details goes here
    context = {
        'order': 'example_order_data',
        'status': 'Shipped'  # Replace with actual data fetching
    }
    return render(request, 'orderdetails.html', context)

def parcel_creation(request):
    return render(request, 'parcelcreation.html')