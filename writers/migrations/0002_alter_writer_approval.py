# Generated by Django 4.1 on 2022-08-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("writers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="writer",
            name="approval",
            field=models.BooleanField(verbose_name="작가등록여부"),
        ),
    ]
