from django.db import models

# Create your models here.


class Subscribers(models.Model):
    subscribers_email = models.EmailField()

    def __str__(self):
        return self.subscribers_email
