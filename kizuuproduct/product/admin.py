from django.contrib import admin
from .models import Product, Category



@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        'id',
        'name',
        'slug',
        'description',
        'poster',
        'is_active',
        'created_at',
        'updated_at',

    ]


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        'id',
        'name',
        'slug',
        'description',
        'price',
        'poster',
        'image',
        'weight',
        'is_active',
        'category',
        'created_at',
        'updated_at',

    ]
