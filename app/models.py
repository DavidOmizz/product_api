from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tags')
    image = models.ImageField(upload_to='product_images', height_field=None, width_field=None, max_length=None)
    price = models.DecimalField(max_digits = 8, decimal_places=2)
    quantity = models.IntegerField()
    ratings = models.DecimalField(max_digits = 5 ,decimal_places = 2)

    def __str__(self):
        return self.name
