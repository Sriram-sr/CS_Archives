# Generated by Django 4.0.4 on 2022-05-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
