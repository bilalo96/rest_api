from django.shortcuts import render
from rest_framework.views import APIView #APIView class
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status #list of http code use when return response and used in post function handle
from rest_framework.authentication import TokenAuthentication # type of authentication we are use
from profiles_api import serializers #to tell apiview what expect when make post , put,..
from profiles_api import models
from profiles_api import permissions
# Create your views here.

class HelloApiView(APIView):
    """"Test Api View"""
    serializer_class =serializers.HelloSerializer

    def get(self,request,format=None):
        """"Return a list of APIView """
        an_apiview=[
          'User HTTP methods as function (get,post,patch,put,delete)',
          'Is similar to a traditional Django View',
          'Gives you the most control over you application logic',
          'Is mapped manually to URls',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
    def post(self,request):
       """Create a hello message with our name """
       serializer=self.serializer_class(data=request.data)#serializer_class:function come with APIView that retrive the configures serializer class  for our view APIView that retrive the configures serializer class
       if serializer.is_valid():
            name=serializer.validated_data.get('name') #name:field that we declared
            message=f'Hello{name}'
            return Response({'message':message})
       else:
            return Response(serializer.errors,
             status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request,pk=None):
        """Handle Updating an object"""
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        """Handle a partial Update of an object"""
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self,request):
        """Return a hello message """
        a_viewset=[
        'Uses actions(list,create,retrieve,updata,partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functoionality with less code',
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})


#create a view set to access the serilizer through an endpoint
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer#assigned serializer_class to model serilizer and queryset to help django to know the standard function like partial_updata , create , etc
    queryset=models.UserProfile.objects.all() #viewset going to manage through this model
    authentication_class=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
