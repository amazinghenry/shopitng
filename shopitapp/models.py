from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.

# >>> drop down menu <<<


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Brand(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand


class Condition(models.Model):
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.condition


class Screensize(models.Model):
    screensize = models.CharField(max_length=100)

    def __str__(self):
        return self.screensize


class Operating_system(models.Model):
    operating_system = models.CharField(max_length=100)

    def __str__(self):
        return self.operating_system


class Color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color


class Ram(models.Model):
    ram = models.CharField(max_length=100)

    def __str__(self):
        return self.ram


class Storage(models.Model):
    storage = models.CharField(max_length=100)

    def __str__(self):
        return self.storage


class CarouselImage(models.Model):
    carousel_image = models.ImageField(upload_to="images/")


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, db_index=True)
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(
        max_digits=10, decimal_places=0, validators=[MinValueValidator(1)])
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    screensize = models.ForeignKey(Screensize, on_delete=models.CASCADE)
    operating_system = models.ForeignKey(
        Operating_system, on_delete=models.CASCADE, null=True)
    color = models.ForeignKey(Color, on_delete=CASCADE)
    ram = models.ForeignKey(
        Ram, on_delete=models.CASCADE, null=True, blank=True)
    storage = models.ForeignKey(
        Storage, on_delete=models.CASCADE, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    product_image1 = models.ImageField(
        upload_to="images/", blank=True, null=True, default='default_img.jpg')
    product_image2 = models.ImageField(
        upload_to="images/", blank=True, null=True, default='default_img.jpg')
    product_image3 = models.ImageField(
        upload_to="images/", blank=True, null=True, default='default_img.jpg')
    agent = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('shopitapp:product-detail', kwargs={'pk': self.pk})


class FeaturedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)
