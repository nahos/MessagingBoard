# Generated by Django 3.0.8 on 2020-07-16 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200716_1616'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='posts',
            unique_together={('name', 'board')},
        ),
    ]
