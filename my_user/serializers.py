from .models import User
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,label ='Password', required=True,style ={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        email=attrs['email']
        password = attrs['password']
        if email and User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email': 'Email address must be unique'})
        return attrs

class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','phone']