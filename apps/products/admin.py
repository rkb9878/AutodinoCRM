from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','category']
    list_filter = ['category']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort_description', 'category', 'subCategory']
    list_filter = ['category', 'subCategory']

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    list_filter = ['product']