from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list pf APIView features"""
        an_apiview=[
        'users http method as function(get, post, put,patch, delete',
        'Is similar to a traditional Django View',
        'Gives you most control of your application logic',
        "Is mapped manually to URLs",
        ]
        return Response({'message':"hello!", "an_apiview": an_apiview})
