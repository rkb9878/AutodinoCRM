# Generated by Django 3.2.8 on 2021-10-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211009_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sort_description',
            field=models.TextField(default='e'),
            preserve_default=False,
        ),
    ]
