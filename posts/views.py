from django.shortcuts import render
from rest_framework import viewsets
from.models import Post
from django.contrib.auth import get_user_model
from .serializers import PostSerializer,Userserializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = Userserializer



