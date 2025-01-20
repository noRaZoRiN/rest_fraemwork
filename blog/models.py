from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="category_icons/", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Publication(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='publications'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='publications'
    )
    image = models.ImageField(upload_to="publications/", null=True, blank=True)
    content = models.CharField(max_length=2500)
    is_archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)