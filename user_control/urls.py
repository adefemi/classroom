from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path, include


myrouter = DefaultRouter(trailing_slash=False)

myrouter.register('users', UserViewSet, 'user_control')


urlpatterns = [
    path('', include(myrouter.urls)),
]
