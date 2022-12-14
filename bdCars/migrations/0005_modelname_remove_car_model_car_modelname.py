# Generated by Django 4.1.4 on 2022-12-14 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bdCars', '0004_car_model_alter_car_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='model',
        ),
        migrations.AddField(
            model_name='car',
            name='modelName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bdCars.modelname'),
        ),
    ]
