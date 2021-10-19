from re import T
from django.db import models
from django.db.models import indexes
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import BooleanField
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
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


class Display(models.Model):
    display = models.CharField(max_length=100)

    def __str__(self):
        return self.display


class FrontCamera(models.Model):
    frontcamera = models.CharField(max_length=100)

    def __str__(self):
        return self.frontcamera


class BackCamera(models.Model):
    backcamera = models.CharField(max_length=100)

    def __str__(self):
        return self.backcamera


class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location



# models for product


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, db_index=True)

    slug = models.SlugField(max_length=200)

    price = models.DecimalField(
        max_digits=10, decimal_places=0, validators=[MinValueValidator(1)])

    description = models.TextField(null=True, blank=True)

    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True)

    condition = models.ForeignKey(
        Condition, on_delete=models.CASCADE, null=True, blank=True)

    screensize = models.ForeignKey(
        Screensize, on_delete=models.CASCADE, null=True, blank=True)

    operating_system = models.ForeignKey(
        Operating_system, on_delete=models.CASCADE, null=True, blank=True)

    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, null=True, blank=True)

    frontcamera = models.ForeignKey(
        FrontCamera, on_delete=models.CASCADE, null=True, blank=True)

    backcamera = models.ForeignKey(
        BackCamera, on_delete=models.CASCADE, null=True, blank=True)

    display = models.ForeignKey(
        Display, on_delete=models.CASCADE, null=True, blank=True)

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

    vip = models.BooleanField(default=False)

    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(name='NewGinIndex', fields=['title']),
        ]

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

# model for leaderboard advert


class Leaderboard(models.Model):
    leaderbanner1 = models.ImageField(
        upload_to="images/leaderbanners", blank=True, null=True, default='banner_default.jpg')
    leaderbanner2 = models.ImageField(
        upload_to="images/leaderbanners", blank=True, null=True, default='banner_default.jpg')
    leaderbanner3 = models.ImageField(
        upload_to="images/leaderbanners", blank=True, null=True, default='banner_default.jpg')
