# Generated by Django 4.1.5 on 2023-02-11 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
