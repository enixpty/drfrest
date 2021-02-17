#Django
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings

#django REST framework
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


#Models User
from authentication.models.user import User

# Serializers
from authentication.serializers.users import ( 
    RegisterSerializer,
    EmailVerificactionSerializer,
    LoginSerializer,
    ResetPasswordEmailRequestSerializer
)

#utils 
import jwt
from utils.send_email import send
#renders
from authentication.renderers import UserRenderer

class RegisterView(generics.GenericAPIView):
    
    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer, )

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        # filter user data with email
        user = User.objects.get(email=user_data['email'])
        #generate token 
        token = RefreshToken.for_user(user).access_token
        
        relativeLink = reverse('auth:email-verify')
        current_site = get_current_site(request).domain
      
        absurl = 'http://'+ current_site+relativeLink+"?token="+str(token)

        email_body = 'Hi ' + user.username+ ' Use link below to verify your email \n ' + absurl

        data = {
           'email_body' : email_body, 
           'to_email' : user.email,
           'email_subject' : 'Verify your email'
        }

        # send email for active user
        send.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(views.APIView):
    """ view when user done the verification """
    def get(self, request):
        
        serializer_class = EmailVerificactionSerializer
        token = request.GET.get('token')
        
        try:
          algorithm = getattr(settings, 'JWT_ENC_ALGORITHM', 'HS256')
          payload = jwt.decode(token, settings.SECRET_KEY, algorithms=algorithm)

          user = User.objects.get(id=payload['user_id'])

          if not user.is_verified :

            user.is_verified = True
            user.save()

          return Response({'email' : 'Successfully activated'},status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as i:
            return Response({'error' : 'Activation Expired'}, status.HTTP_400_BAD_REQUEST)

        except jwt.exceptions.DecodeError as i:
            print(i)
            return Response({'error' : 'Invalid token'}, status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):
    """ Login view """

    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):

    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):

        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)

  