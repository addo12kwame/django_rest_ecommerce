from rest_framework import viewsets,status,mixins,generics
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .message import Message
from .models import Product
from .serializer import ProductSerializer,MessageSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Add this decorator to restrict api view if you are not logged in
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def list_products(request):
    all_products = Product.objects.all()
    serializer = ProductSerializer(all_products,many=True)
    return Response(data=serializer.data)

@api_view(['GET','POST'])
@authentication_classes([SessionAuthentication,BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_messages(request):
    """
    Function based authentication done here by adding authentication_classes decorator and permission classes decorator
    :param request:
    :return:
    """
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


class ListProductsMixins(mixins.ListModelMixin,generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class DetailedProductMixins(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ListProductsGenerics(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailedProductsGenerics(generics.RetrieveAPIView,generics.DestroyAPIView,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SpecialProductsGenerics(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    """
    Classed  based authentication is done here by setting authentication_classes and permission_classes
    """
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer