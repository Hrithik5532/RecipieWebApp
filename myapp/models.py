from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Recipe(models.Model):
    
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = RichTextField()
    ingre = RichTextField()
    steps =RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img = models.FileField(upload_to='recipe_img/')

    def get_absolute_url(self):
      return reverse("recipes-detail", kwargs={"pk": self.pk})
    def __str__(self):
        return self.title
