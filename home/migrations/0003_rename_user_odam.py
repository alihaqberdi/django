# Generated by Django 4.1.5 on 2023-01-04 15:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_remove_user_savat_user_savat'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='odam',
        ),
    ]
