# Generated by Django 3.2.7 on 2022-02-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220207_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes_phones',
        ),
        migrations.RemoveField(
            model_name='product',
            name='has_sizes_tv',
        ),
        migrations.AddField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]