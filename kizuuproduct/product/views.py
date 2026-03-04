from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductListApiView(generics.ListAPIView):
    """

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateApiView(generics.CreateAPIView):
    """

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailApiView(generics.RetrieveAPIView):
    """

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class CategoryListApiView(generics.ListAPIView):
    """

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateApiView(generics.CreateAPIView):
    """

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateApiView(generics.UpdateAPIView):
    """

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailApiView(generics.RetrieveAPIView):
    """

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteApiView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer