# Generated by Django 3.2 on 2024-09-20 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20240919_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
    ]
