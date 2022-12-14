# Generated by Django 3.2.6 on 2022-10-12 17:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_recipe_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingre',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=500),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
