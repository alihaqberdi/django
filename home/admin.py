from django.contrib import admin
from .models import Product, odam
# Register your models here.

admin.site.register([Product, odam])
