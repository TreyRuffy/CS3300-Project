# Generated by Django 4.2.6 on 2023-10-31 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs3300_project', '0004_alter_horse_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
