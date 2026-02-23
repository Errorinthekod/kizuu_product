from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer




class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
