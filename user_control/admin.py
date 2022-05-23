from django.contrib import admin
from .models import CustomUser, UserProfile, Student, Teacher, FileUpload, ActiveRole


admin.site.register((CustomUser, UserProfile, Student, Teacher, FileUpload, ActiveRole))
