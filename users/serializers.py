from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Municipality, Department, Location

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
    
class MunicipalitySerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Municipality
        fields=[
            'name',
            'department'
        ]

class DepartmentSerializer(serializers.ModelSerializer):
    municipalities = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = [
            'department_id',
            'name',
            'municipalities'
        ]

    def get_municipalities(self, obj):
        municipalities = Municipality.objects.filter(department=obj)
        return MunicipalitySerializer(municipalities, many=True).data

class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)
        token['user_type']= User.user_type
        token['username']= User.username
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_type'] = self.user.user_type
        data['username'] = self.user.username
        return data

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'location_id', 
            'latitude', 
            'longitude'
            ]
