from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Product(models.Model):
    title=models.CharField(max_length=50)
    discription=models.TextField()
    price=models.IntegerField()
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag)

class Review(models.Model):
    text= models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

