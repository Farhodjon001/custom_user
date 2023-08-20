from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from .serialiers import CustomUserSerializers
from rest_framework.permissions import IsAuthenticated


from .models import CustomUser
# Create your views here.

class CustomUserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers

