from django.urls import path

from . import views

urlpatterns = [

    # Products
    path('product_list/', views.ProductListApiView.as_view(), name='product-list'),
    path('product_create/', views.ProductCreateApiView.as_view(), name='product-create'),
    path('product_update/<int:pk>/', views.ProductUpdateApiView.as_view(), name='product-update'),
    path('product_detail/<int:pk>/', views.ProductDetailApiView.as_view(), name='product-detail'),
    path('product_delete/<int:pk>/', views.ProductDeleteApiView.as_view(), name='product-delete'),

    # Categories
    path('cat_list/', views.CategoryListApiView.as_view(), name='category-list'),
    path('cat_create/', views.CategoryCreateApiView.as_view(), name='category-create'),
    path('cat_update/<int:pk>/', views.CategoryUpdateApiView.as_view(), name='category-update'),
    path('cat_detail/<int:pk>/', views.CategoryDetailApiView.as_view(), name='category-detail'),
    path('cat_delete/<int:pk>/', views.CategoryDeleteApiView.as_view(), name='category-delete'),
]