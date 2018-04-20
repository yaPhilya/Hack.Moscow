from django.db import models


class Object(models.Model):
    name = models.TextField()
    path = models.TextField()