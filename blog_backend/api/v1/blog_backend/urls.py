from django.urls import path
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('reg/', UserReg.as_view(), name="reg"),
    path('login/', ObtainAuthToken.as_view(), name="login"),
    path('user-update/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('blog-posts/', BlogPostList.as_view(), name="blog"),
    path('blog-posts/<int:pk>/', BlogPostDetail.as_view(), name="blog-edit"),

]

