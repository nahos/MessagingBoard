# Generated by Django 3.0.8 on 2020-07-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]