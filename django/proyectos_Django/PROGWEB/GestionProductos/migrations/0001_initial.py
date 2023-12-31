# Generated by Django 4.2.2 on 2023-06-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('fecha', models.DateField()),
                ('producto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=30)),
                ('origen', models.CharField(max_length=50)),
                ('caducacion', models.DateField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
