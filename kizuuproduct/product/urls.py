from django.urls import path

from . import views

urlpatterns = [

    path('list/', views.ProductListApiView.as_view(), name='product-list'),
]