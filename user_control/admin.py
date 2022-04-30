from django.contrib import admin
from .models import CustomUser, UserProfile, Student, Teacher, FileUpload


admin.site.register((CustomUser, UserProfile, Student, Teacher, FileUpload))
