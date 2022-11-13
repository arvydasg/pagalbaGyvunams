# Generated by Django 4.1.3 on 2022-11-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gyvuneliai", "0008_alter_animal_sex"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="good_with_cats",
            field=models.CharField(
                blank=True,
                help_text="Trumpai",
                max_length=100,
                null=True,
                verbose_name="Ar draugauja su katėmis?",
            ),
        ),
        migrations.AddField(
            model_name="animal",
            name="good_with_dogs",
            field=models.CharField(
                blank=True,
                help_text="Trumpai",
                max_length=100,
                null=True,
                verbose_name="Ar draugauja su šunimis?",
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="sex",
            field=models.CharField(
                choices=[("Patinas", "Patinas"), ("Patelė", "Patelė")],
                default="Patinas",
                max_length=10,
                verbose_name="Lytis",
            ),
        ),
    ]