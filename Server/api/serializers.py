from rest_framework import serializers
from .models import CustomUser, Categories, Colors, Icons, Tasks
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSlidingSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(required=True)
    # name = serializers.CharField(max_length=50, required=True)
    # password = serializers.CharField(
    #     write_only=True,
    #     required=True
    # )
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password')
        
    def validate_email(self, value):
        user = CustomUser.objects.filter(email=value)
        if len(user):
            raise serializers.ValidationError("Email already exists!")
        return value
    
    def validate_name(self, value):
        user = CustomUser.objects.filter(name=value)
        if len(user):
            raise serializers.ValidationError("User name already exists!")
        return value
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return CustomUser.objects.create(**validated_data)
    
class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["name"] = user.name
        token['email'] = user.email
        return token
    
class UserTokenObtainSlidingPairSerializer(TokenObtainSlidingSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["name"] = user.name
        token['email'] = user.email
        return token

class ColorSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=50)
    
    class Meta:
        model = Colors
        fields = ['code', 'name']
        
class IconSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=10)
    symbol = serializers.CharField(max_length=50)
    
    class Meta:
        model = Icons
        fields = ['code', 'symbol']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'color', 'icon', 'isEditable', 'user']
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'name', 'categoryId', 'isCompleted', 'date_created', 'dateTimeDone', 'user']