from rest_framework.views import APIView
from .serializers import *
from blog_app.models import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class UserReg(APIView):
    serializer_class = UserRegSerializer

    def post(self, request):
        serializer = UserRegSerializer(data=request.data)

        try:
            if serializer.is_valid():
                user = serializer.save()  # Call the create method defined in the serializer
                return Response({'message': 'Registered successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserUpdate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer

    def put(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            # Fetch the user by ID
            user_instance = Customuserdb.objects.get(id=id)
        except Customuserdb.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


        serializer = UserUpdateSerializer(instance=user_instance, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            posts = BlogPost.objects.all()
            serializer = BlogPostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.validated_data['author'] = request.user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BlogPostDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            post = get_object_or_404(BlogPost, pk=pk)
            serializer = BlogPostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BlogPost.DoesNotExist:
            return Response({'error': 'BlogPost not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            post = get_object_or_404(BlogPost, pk=pk)
            serializer = BlogPostSerializer(instance=post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BlogPost.DoesNotExist:
            return Response({'error': 'BlogPost not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            post = get_object_or_404(BlogPost, pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BlogPost.DoesNotExist:
            return Response({'error': 'BlogPost not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

