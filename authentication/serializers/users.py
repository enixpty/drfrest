""" User serializers """

#Django 
from django.contrib import auth
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

#Django REST Framework
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

# Model User
from authentication.models.user import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    #Name 
    first_name = serializers.CharField(min_length=2)
    last_name =  serializers.CharField(min_length=2)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name','last_name']
    
    def  validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contains alphanumeric character')

        return attrs

    
    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)


class EmailVerificactionSerializer(serializers.ModelSerializer):

    token = serializers.CharField(max_length=800)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=100, min_length=8, write_only=True)
    username = serializers.CharField(max_length=60, min_length=3, read_only=True)
    tokens = serializers.CharField(max_length=68, min_length=8,  read_only=True)

    class Meta:
        model = User
        fields= ['email','password','username','tokens'] 

    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credential, try again')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')


        return  {
            'email' : user.email,
            'username' : user.username,
            'tokens' :  user.tokens
        }
        
        return super().validate(attrs)


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']

    def validate(self, attrs):

        try:
            email = attrs.get('email','')
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                uidb64 = urlsafe_base64_encode(user.id)
                token = PasswordResetTokenGenerator().make_token(user)
                


            return attrs

        except Exception as identifier:
            pass

        return super().validate(attrs)

