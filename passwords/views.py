from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Password
from .serializers import PasswordSerializer

class ListPasswords(APIView):
    
    def get(self, request):
        passwords = Password.objects.all()
        serializer = PasswordSerializer(passwords,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)