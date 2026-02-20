from rest_framework import generics
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer




class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer