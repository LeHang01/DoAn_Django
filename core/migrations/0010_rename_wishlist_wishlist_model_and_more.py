# Generated by Django 4.2.11 on 2024-04-13 21:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_address_mobile_alter_cartorder_product_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='wishlist',
            new_name='wishlist_model',
        ),
        migrations.AlterModelOptions(
            name='wishlist_model',
            options={'verbose_name_plural': 'wishlists'},
        ),
    ]
