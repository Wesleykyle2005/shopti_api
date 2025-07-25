from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= [
            'username',
            'email',
        ]

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields= [
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {
            'password': {
                'write_only':True 
            }
        }

    def create(self, validate_data):
        user= User.objects.create_user(**validate_data)
        return user