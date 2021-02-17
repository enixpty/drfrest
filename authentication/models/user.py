""" user models """
#django
from django.db import models

#django REST Framework
from rest_framework_simplejwt.tokens import RefreshToken

# Generic Base model  
from utils.models import GenericModel

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):

    def create_user(self, username, email, first_name, last_name, password=None):

        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a email')
        if first_name is None:
            raise TypeError('First Name should not be none')
        if last_name is None:
            raise TypeError('Last Name should not be none')

        user  = self.model(username=username, email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, first_name, last_name):
        if password is None:
            raise TypeError('Password should not be none')
        
        user = self.create_user(username, email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, GenericModel ):
    """ class users """

    username = models.CharField(
            'Username', 
            max_length=255, 
            unique=True, 
            db_index=True
        )

    first_name = models.CharField(
            'First Name', 
            blank=True,
            max_length=60 
        )

    last_name = models.CharField(
            'Last name',  
            blank=True,
            max_length=60
        )

    email = models.EmailField( 
        'email address', 
        unique=True,  
        db_index=True,
        error_messages={
            'unique' : 'Email already exists'
        }
    )

    is_verified = models.BooleanField( "user is verified", default= False )
    
    is_active = models.BooleanField( "user is active", default= True )    

    is_staff = models.BooleanField( "user is staff",  default= False  )
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh' : str(refresh),
            'access'  : str(refresh.access_token)
        }
    