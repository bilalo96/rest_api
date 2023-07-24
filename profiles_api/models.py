from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManger(BaseUserManager):
    """Manger for user profiles"""

    def create_user(self,email,name,password=None):
        """"Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.ser_password(password)
        user.save(using=self.db)

        return user
    def create_superuser(self,email,name,password):
        """" Create and save a new superuser with givendetails"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)

        return user

# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """"Database model for useres in the system"""
    email=models.EmailField(max_length=200,unique=True)
    name=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManger()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """"Retrieve full name of useres"""
        return self.name

    def get_short_name(self):
        """"Retrieve short name of useres"""
        return self.name

    def __str__(self):
        """Return string representation of our user """
        return self.email
