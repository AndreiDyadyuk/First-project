# Generated by Django 4.1.2 on 2022-10-23 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_delete_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='description',
        ),
    ]