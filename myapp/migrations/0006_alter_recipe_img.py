# Generated by Django 3.2.6 on 2022-10-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_recipe_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='img',
            field=models.ImageField(upload_to='recipe_img/'),
        ),
    ]
