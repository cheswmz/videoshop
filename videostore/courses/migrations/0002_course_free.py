# Generated by Django 3.1 on 2020-08-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='free',
            field=models.BooleanField(default=True),
        ),
    ]
