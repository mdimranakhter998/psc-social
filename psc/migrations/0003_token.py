# Generated by Django 3.2.7 on 2021-10-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psc', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
    ]
