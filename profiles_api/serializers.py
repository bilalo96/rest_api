from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView"""
    name=serializers.CharField(max_length=10)

#serilizer for profile api
                                                      #ModelSerializer allow to make simple object in the database because that we use create function
class UserProfileSerializer(serializers.ModelSerializer):#pass ModelSerializer to use metaclass to configure the serilizer to point to a specific model
    """Serializes a User profile object"""

    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')#1-we need exiption to password because we need just when we add user in the system,we don't to allow user to retrive the password hash because there are security risk with that,so we make the password fields write only
        extra_kwargs={ #extra_kwargs to apply specific commint 1
         'password':{
             'write_only':True,
             'style':{'input_type':'password'}
         }
        }
        #we ovverride the create function because the password gets created as a hash and not the clear text password that it would do by default
def create(self,validated_data):
       """Create and return a new user"""
       user=models.UserProfile.objects.create_user(
         email=validated_data['email'],
         name=validated_data['name'],
         password=validated_data['password']
       )
       return user
