# Generated by Django 4.1.5 on 2023-02-23 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
