from django.db import models


# Create your models here.
class Link(models.Model):
    uuid = models.CharField(max_length=10, unique=True, null=False)
    origin_link = models.CharField(max_length=200, unique=False, null=False)
