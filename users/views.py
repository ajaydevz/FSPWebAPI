from .serializers import UserSerializer,myTokenObtainPairSerializer
from .models import UserAccount
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.


class  MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer


