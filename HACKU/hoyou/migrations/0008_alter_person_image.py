# Generated by Django 4.2.5 on 2023-09-05 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hoyou", "0007_person_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="image",
            field=models.ImageField(default=None, null=True, upload_to=""),
        ),
    ]
