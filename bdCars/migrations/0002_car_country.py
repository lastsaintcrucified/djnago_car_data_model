# Generated by Django 4.1.4 on 2022-12-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdCars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='country',
            field=models.CharField(max_length=45, null=True),
        ),
    ]