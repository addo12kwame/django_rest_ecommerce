from itertools import product

from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
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


class ListProducts(APIView):
    def get(self,request):
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products,many=True)
        return Response(data=serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
            return Response({"Success": f"Product {product_saved.name} created successfully"}, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailedView(APIView):
    def get(self,request,id):
        all_products = Product.objects.get(product_id=id)
        serializer = ProductSerializer(all_products,)
        return Response(data=serializer.data)

    def put(self,request,id):
        product_obj = Product.objects.get(product_id=id)

        # Pass the instance of the thing you want to update
        serializer = ProductSerializer(instance=product_obj,data=request.data)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
            return Response({"Success": f"Product {product_saved.name} updated successfully"}, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        product_to_be_deleted = Product.objects.get(product_id=id)
        product_to_be_deleted.delete()
        return Response(status=status.HTTP_200_OK)
