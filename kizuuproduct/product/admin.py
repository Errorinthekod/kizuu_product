from django.contrib import admin
from .models import Product, Category, User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'email',
                    'date_joined',
                    'last_login'
                    )

    list_fiter = (
                    'is_staff',
                    'is_active',
                    'is_superuser'
    )

    search_fields = ('username', 'email')
    ordering = ('username', 'email')


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
