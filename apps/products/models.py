from django.db import models
from utils.utils import StatusMixin

from utils.mediaPath import *


class Category(StatusMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=categoryImage)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Cateogry"


class SubCategory(StatusMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=subCategoryImage, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SubCategory"


class Product(StatusMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    sort_description = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Products"
        verbose_name = "Products"


class ProductImages(StatusMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=productImage)

    def __str__(self):
        return str(id)

    class Meta:
        db_table = "ProdcutImages"


