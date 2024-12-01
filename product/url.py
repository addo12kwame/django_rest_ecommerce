from django.urls import path

from product.views import list_products, list_messages

urlpatterns  = [
    path('products/', list_products, name='products'),
    path('messagelist/', list_messages, name='messagelist'),

]