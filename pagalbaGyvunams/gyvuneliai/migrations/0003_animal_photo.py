# Generated by Django 4.1.3 on 2022-11-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gyvuneliai", "0002_animal_delete_blog_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="photo",
            field=models.ImageField(blank=True, upload_to="photo/%Y/%m%d"),
        ),
    ]
