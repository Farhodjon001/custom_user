from django.urls import path
from  .views import BookCreateAPIView,BookListAPIView

urlpatterns=[
    path('all/',BookListAPIView.as_view()),
    path("create/",BookCreateAPIView.as_view()),
]