# Generated by Django 3.2.6 on 2022-10-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_img_gallary_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='img',
            field=models.FileField(default=False, null=True, upload_to='recipe_img/'),
        ),
        migrations.DeleteModel(
            name='img_gallary',
        ),
    ]