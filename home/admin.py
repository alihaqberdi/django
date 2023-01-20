from django.contrib import admin
from  .models import Women, Categories
# Register your models here.

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = 'title', 'content', 'time_create', 'time_update', 'is_published', 'cat'


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = 'name',
