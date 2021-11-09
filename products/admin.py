from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'category',
        'price',
        'main_image',
        'rating',
    )
    ordering = ('id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'friendly_name'
    )
    ordering = ('id',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
