# Generated by Django 4.0.5 on 2022-09-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1, null=True),
        ),
    ]
