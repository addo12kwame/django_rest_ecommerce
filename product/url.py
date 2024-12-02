from django.urls import path

from product.views import list_products, list_messages, ListProducts, ProductDetailedView, ListProductsMixins, \
    DetailedProductMixins

urlpatterns  = [
    path('products/', list_products, name='products'),
    path('messagelist/', list_messages, name='messagelist'),
    path('classproductlist/', ListProducts.as_view(),name='listProducts'),
    path('classdetailedproduct/<int:id>', ProductDetailedView.as_view(),name='detailedProduct'),
    path('mixinpath/', ListProductsMixins.as_view(),name='mixingpath'),
    path('detailedmixin/<int:pk>', DetailedProductMixins.as_view(),name='mixindetail'),


]