from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import BookCreatePermission

from .models import Book
# Create your views here.

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,BookCreatePermission)
