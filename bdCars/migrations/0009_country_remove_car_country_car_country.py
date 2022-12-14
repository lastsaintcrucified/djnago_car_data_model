# Generated by Django 4.1.4 on 2022-12-14 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdCars', '0008_owner_company_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='country',
        ),
        migrations.AddField(
            model_name='car',
            name='country',
            field=models.ManyToManyField(to='bdCars.country'),
        ),
    ]
