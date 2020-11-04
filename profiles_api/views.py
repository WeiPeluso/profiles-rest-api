from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets



from profiles_api import serializers
from profiles_api import models

class HelloAPiView(APIView):
    """Test API View"""

    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list pf APIView features"""
        an_apiview=[
        'uses http method as function(get, post, put,patch, delete',
        'Is similar to a traditional Django View',
        'Gives you most control of your application logic',
        "Is mapped manually to URLs",
        ]
        return Response({'message':"hello!", "an_apiview": an_apiview})

    def post(self,request):
        """create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'put'})

    def patch(self,request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """Delete an object'"""
        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """return a hello messge"""
        a_viewset=[
        'uses action(list, create,retrieve, update, partial_update, destroy)',
        'Automatically maps to URLS using Routers',
        'provides more functionality with less code',
        ]
        return Response({'message':"hello!", "an_viewset": a_viewset})

    def create(self,request):
        """create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'method':'retrieve'})

    def update(self,request, pk=None):
        """Handle updating of an object"""
        return Response({'method':'update'})

    def partial_update(self,request,pk=None):
        """handle paritial updating an object'"""
        return Response({'method':'partial_update'})

    def destroy(self,request,pk=None):
        """handle removing an object'"""
        return Response({'method':'destroy'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handel creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    
