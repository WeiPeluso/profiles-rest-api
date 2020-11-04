from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloAPiView(APIView):
    """Test API View"""

    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list pf APIView features"""
        an_apiview=[
        'users http method as function(get, post, put,patch, delete',
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
