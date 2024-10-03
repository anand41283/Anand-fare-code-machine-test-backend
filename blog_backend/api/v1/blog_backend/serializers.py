from rest_framework import serializers
from blog_app.models import *

class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuserdb  # Use your custom user model
        fields = ['username', 'first_name', 'last_name', 'password', 'profile_pic']
        extra_kwargs = {
            'password': {'write_only': True}  # Password should be write-only
        }

    def create(self, validated_data):
        user = Customuserdb(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            profile_pic=validated_data.get('profile_pic', None)
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuserdb
        fields = ['username', 'first_name', 'last_name', 'profile_pic']


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags', 'author']

