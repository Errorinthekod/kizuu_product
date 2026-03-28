from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import User
from .serializers import UserSerializer



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer()
    permission_classes = [IsAdminUser]

class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer()
    permission_classes = [IsAdminUser]
