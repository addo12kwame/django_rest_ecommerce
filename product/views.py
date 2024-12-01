
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .message import Message
from .models import Product
from .serializer import ProductSerializer,MessageSerializer

# Add this decorator to restrict api view if you are not logged in
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def list_products(request):
    all_products = Product.objects.all()
    serializer = ProductSerializer(all_products,many=True)
    return Response(data=serializer.data)

@api_view(['GET','POST'])
def list_messages(request):
    message_obj = Message(email='kwame@gmail.com',content='Hi Kwame')
    serializer = MessageSerializer(message_obj)
    print(serializer.data)

    return Response(serializer.data)



