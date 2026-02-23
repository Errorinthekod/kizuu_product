from django.urls import path

from . import views

urlpatterns = [

    path('product_list/', views.ProductListApiView.as_view(), name='product-list'),
    path('product_create/', views.ProductCreateApiView.as_view(), name='product-create'),
    path('cat_list/', views.CategoryListApiView.as_view(), name='category-list'),
    path('cat_create/', views.CategoryCreateApiView.as_view(), name='category-create'),

]