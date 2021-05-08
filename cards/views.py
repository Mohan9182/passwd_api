from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Card
from .serializers import CardSerializer

# Create your views here.
class ListCards(APIView):
    
    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)