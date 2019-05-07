from django.db import models

# Create your models here.
class Post(models.Model):
    title_JUNGBONG = models.TextField()
    content_dongsik = models.CharField(max_length=100)
    bong = models.CharField(max_length=100)
