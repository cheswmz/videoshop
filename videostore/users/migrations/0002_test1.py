# Generated by Django 3.1 on 2020-08-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], default='M', max_length=1)),
                ('agree', models.BooleanField(default=False, verbose_name='Соглашение на отправку уведомлений на почту')),
            ],
            options={
                'verbose_name': 'test',
                'verbose_name_plural': 'tests',
            },
        ),
    ]
