from django.shortcuts import render,get_object_or_404,redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from .serializerz import *
from rest_framework.views import APIView
from .models import *
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
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

def signup_page(request):
    return render(request, 'signup.html')


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # Save the user, this will also hash the password
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    print("USer",user)
    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#log out
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            # Get the refresh token from the request
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)

            # Blacklist the refresh token
            token.blacklist()
            return redirect('login')
            # return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def order_details(request):
    # Logic to fetch order details goes here
    context = {
        'order': 'example_order_data',
        'status': 'Shipped'  # Replace with actual data fetching
    }
    return render(request, 'orderdetails.html', context)




def parcel_creation(request):
    return render(request, 'parcelcreation.html')


@api_view(['POST'])
def createParcel(request):
    if not request.user.is_authenticated:
        return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = ParcelSerializer(data=request.data)
    if serializer.is_valid():
        parcel = serializer.save()

        # Create a TransactionLog entry
        status_message = f"Added parcel from {parcel.sender_name} to {parcel.recipient_name}"
        TransactionLog.objects.create(parcel=parcel, status=status_message)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_parcel_status(request, tracking_number):
    try:
        parcel = Parcel.objects.get(tracking_number=tracking_number)
    except Parcel.DoesNotExist:
        return Response({'detail': 'Parcel not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ParcelSerializer(parcel, data=request.data, partial=True)
    if serializer.is_valid():
        parcel = serializer.save()
        status_message = f"Updated status to {parcel.status}"
        TransactionLog.objects.create(parcel=parcel, status=status_message)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def allParcel(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    search_query = request.GET.get('search', '')  
    print("search_query",search_query)
    parcels = Parcel.objects.filter(
        Q(parcel_name__icontains=search_query) | Q(id__icontains=search_query)
    )
    print("parrrrrrrr",parcels)
    # Serialize and return the filtered parcels
    serializer = ParcelSerializer(parcels, many=True)
    return Response({'parcels': serializer.data}, status=status.HTTP_200_OK)



def order_info(request, tracking_number):
    parcel = get_object_or_404(Parcel, tracking_number=tracking_number)
    data = {
        'tracking_number': parcel.tracking_number,
        'parcel_name': parcel.parcel_name,
        'sender_name': parcel.sender_name,
        'recipient_name': parcel.recipient_name,
        'status': parcel.status,
    }
    return JsonResponse({'parcel': data})

def report_table(request):
    parcels = Parcel.objects.all()
    serializer = ParcelSerializer(parcels, many=True)
    context = {
        'parcels': serializer.data
    }
    return render(request,'reports.html',context)


