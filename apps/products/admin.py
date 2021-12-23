from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name']

# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','category', 'parent']
#     list_filter = ['category']

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    pass
@admin.register(Modal)
class ModalsAdmin(admin.ModelAdmin):
    pass
@admin.register(catalogue)
class CatalogsAdmin(admin.ModelAdmin):
    pass
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    list_filter = ['product']