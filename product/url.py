from django.urls import path

from product.views import list_products, list_messages, ListProducts, ProductDetailedView

urlpatterns  = [
    path('products/', list_products, name='products'),
    path('messagelist/', list_messages, name='messagelist'),
    path('classproductlist/', ListProducts.as_view(),name='listProducts'),
    path('classdetailedproduct/<int:id>', ProductDetailedView.as_view(),name='detailedProduct'),


]