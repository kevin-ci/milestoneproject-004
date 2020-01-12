from django.db import models

# Create your models here.
class Category_001(models.Model):
    name = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    url = models.URLField(max_length=250)
    
    def __str__(self):
        return self.name