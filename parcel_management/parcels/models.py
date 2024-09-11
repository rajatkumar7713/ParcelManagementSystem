from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    ROLE_CHOICES = [('admin', 'Admin'), ('manager', 'Manager'), ('customer', 'Customer')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    address=models.TextField(max_length=300)

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
    
    # Override related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Use a unique name for reverse relation
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Use a unique name for reverse relation
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )

# Parcel model
class Parcel(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True)
    sender_name = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=100)
    STATUS_CHOICES = [('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Transaction Log model
class TransactionLog(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

