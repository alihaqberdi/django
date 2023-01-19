from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class odam(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    savat = models.ManyToManyField(Product,)




