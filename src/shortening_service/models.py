from django.db import models


class Link(models.Model):
    generated_id = models.CharField(max_length=10, unique=True, null=False)
    origin_link = models.CharField(max_length=200, unique=False, null=False)
