from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import viewsets
from rest_framework import status
from . import models
from . import permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of APIView feature."""

        an_apiview = [
          'Uses HTTP methods as functions (get, post, patch, put, delete)',
          'Is similar to a traditional Django View',
          'Gives you the most control over your logic',
          'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview })


    def post(self,request):
        """Create hello massage with name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handling Updating objects"""
        return Response({'message':'put'})

    def patch(self,request,pk=None):
        """patch request only provided in the request"""
        return Response({'message':'patch'})

    def delete(self,request,pk=None):
        """ Deleted and objects"""
        return Response({'message':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """Return Hello massage"""
        a_viewset = [
          'Uses HTTP methods as functions (get, post, patch, put, delete)',
          'Is similar to a traditional Django View',
          'Gives you the most control over your logic',
          'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        """create a new hello massage"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
              serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handles getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handles updating part of the object"""
        return Response({'http_method':'PACTH'})

    def destroy(self,request,pk=None):
        """Handle Remove an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handling creating and updateing profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
