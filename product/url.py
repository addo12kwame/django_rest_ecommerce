from django.urls import path
from product.views import list_products, list_messages, ListProducts, ProductDetailedView, ListProductsMixins, \
    DetailedProductMixins, ListProductsGenerics, DetailedProductsGenerics, SpecialProductsGenerics, ProductViewSet
from rest_framework.routers import DefaultRouter


# ViewSets needs routers
router = DefaultRouter()
router.register(
    'productview',ProductViewSet,basename='product'
)

# Router has to be added to the urlpatterns
urlpatterns  = [
    path('products/', list_products, name='products'),
    path('messagelist/', list_messages, name='messagelist'),
    path('classproductlist/', ListProducts.as_view(),name='listProducts'),
    path('classdetailedproduct/<int:id>', ProductDetailedView.as_view(),name='detailedProduct'),
    path('mixinpath/', ListProductsMixins.as_view(),name='mixingpath'),
    path('detailedmixin/<int:pk>', DetailedProductMixins.as_view(),name='mixindetail'),
    path('genlist/', ListProductsGenerics.as_view(),name='genericlist'),
    path('gendetailed/<int:pk>/', DetailedProductsGenerics.as_view(),name='genericdetail'),
    path('genspecial/<int:pk>/', SpecialProductsGenerics.as_view(),name='genericspecial'),


]+router.urls