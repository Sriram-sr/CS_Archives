# Generated by Django 4.0.5 on 2022-06-25 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]