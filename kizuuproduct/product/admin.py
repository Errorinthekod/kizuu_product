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
        'status',
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
        'status',
        'category',
        'created_at',
        'updated_at',

    ]
