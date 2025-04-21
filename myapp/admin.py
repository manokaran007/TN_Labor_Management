from django.contrib import admin
from .models import UserProfile, Complaint

admin.site.register(UserProfile)
admin.site.register(Complaint)