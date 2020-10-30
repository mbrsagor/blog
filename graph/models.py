from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True,  on_delete=models.CASCADE, related_name='product_category')

    def __str__(self):
        return self.name
