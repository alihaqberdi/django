from django.db import models

# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name







