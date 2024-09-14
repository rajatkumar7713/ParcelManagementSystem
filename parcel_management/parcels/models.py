from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string
# Custom user model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    ROLE_CHOICES = [('admin', 'Admin'), ('manager', 'Manager'), ('customer', 'Customer')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    address=models.TextField(max_length=300) #for storing address

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
    tracking_number = models.CharField(max_length=100, unique=True ,blank=True)
    sender_name = models.CharField(max_length=100)
    parcel_name=models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=100)
    STATUS_CHOICES = [('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'),('canceled', 'Canceled')]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_tracking_number(self):
        """Generate a unique tracking number."""
        length = 10
        characters = string.ascii_letters + string.digits
        tracking_number = ''.join(random.choice(characters) for _ in range(length))
        return tracking_number

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = self.generate_tracking_number()
        super().save(*args, **kwargs)

# Transaction Log model
class TransactionLog(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    status = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

