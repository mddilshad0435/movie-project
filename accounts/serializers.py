from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User
from django.contrib.auth import authenticate


class UserRegestrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['email','password','confirm_password','username']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists!.")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("password must be equal to confirm_password")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255,write_only=True)
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )
    token = serializers.DictField(read_only=True)
    class Meta:
        model = User
        fields = ['email','password','token']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email,password=password)
        if not user:
            raise serializers.ValidationError('Invalid Credentials!')
        return {'token':user.get_tokens_for_user()}
        

        