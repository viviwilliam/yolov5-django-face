# Generated by Django 4.1.6 on 2023-03-09 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0002_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="photoDate",
            field=models.ImageField(default="user1.jpg", upload_to="photos"),
        ),
        migrations.AlterField(
            model_name="photo",
            name="priPhotoDate",
            field=models.ImageField(default="user1.jpg", upload_to="photos"),
        ),
    ]
