from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CustomUser, UserSerializer, CreateUserSerializer, UserProfile, UserProfileSerializer,
    Student, StudentSerializer, Teacher, TeacherSerializer, FileUpload, FileUploadSerializer
)
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return UserSerializer
    
    def create(self, request, *args, **kwargs):
        request_serialized = self.get_serializer(data=request.data)
        request_serialized.is_valid(raise_exception=True)
        
        email = request_serialized.validated_data["email"]
        password = request_serialized.validated_data["password"]
        
        user = CustomUser.objects.create_user(email, password)
        
        result = self.serializer_class(user).data
    
        return Response(result, status=status.HTTP_201_CREATED)
    

class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    
    
class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    

class TeacherViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    
    
class FileUploadViewSet(ModelViewSet):
    serializer_class = FileUploadSerializer
    queryset = FileUpload.objects.all()