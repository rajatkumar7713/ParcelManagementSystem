from django.contrib import admin

from .models import CustomUser, Parcel, TransactionLog

admin.site.register(CustomUser)
admin.site.register(Parcel)
admin.site.register(TransactionLog)

