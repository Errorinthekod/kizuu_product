from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class ProductListApiView(generics.ListAPIView):
    """

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductCreateApiView(generics.CreateAPIView):
    """

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class ProductDetailApiView(generics.RetrieveAPIView):
    """

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class CategoryListApiView(generics.ListAPIView):
    """

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryCreateApiView(generics.CreateAPIView):
    """

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class CategoryUpdateApiView(generics.UpdateAPIView):
    """

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryDetailApiView(generics.RetrieveAPIView):
    """

    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryDeleteApiView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]