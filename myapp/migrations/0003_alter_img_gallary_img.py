# Generated by Django 3.2.6 on 2022-10-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_img_gallary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img_gallary',
            name='img',
            field=models.FileField(upload_to='recipe_img/'),
        ),
    ]
