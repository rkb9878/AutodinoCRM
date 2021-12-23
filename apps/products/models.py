from django.db import models
from utils.utils import StatusMixin

from utils.mediaPath import *
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(StatusMixin):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=categoryImage)
    icon = models.ImageField(upload_to=categoryIcon)
    parent = models.ManyToManyField('self', blank=True ,related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Cateogry"


# class SubCategory(StatusMixin):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to=subCategoryImage, null=True, blank=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = "SubCategory"
#         unique_together = ('name', 'parent')

class Brands(StatusMixin):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=brandIcon)
    icon = models.ImageField(upload_to=brandIcon, blank=True, null=True)

    class Meta:
        db_table = "Brands"
        verbose_name = "Brands"
        verbose_name_plural = "Brands"

class Modal(StatusMixin):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=categoryIcon, blank=True, null=True)
    class Meta:
        db_table = "Modals"
        verbose_name = "Modals"
        verbose_name_plural = "Modals"


class catalogue(StatusMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    modal = models.ForeignKey(Modal, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "catalogue"
        verbose_name = "catalogue"
        verbose_name_plural = "catalogue"

class Product(StatusMixin):
    catalogue = models.ForeignKey(catalogue, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sort_description = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    rating_count = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = "Products"
        verbose_name = "Products"
        verbose_name_plural = "Products"
        unique_together = ('catalogue', 'slug')

class ProductImages(StatusMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=productImage)

    def __str__(self):
        return str(id)

    class Meta:
        db_table = "ProdcutImages"
        verbose_name_plural = "Prodcut Images"


