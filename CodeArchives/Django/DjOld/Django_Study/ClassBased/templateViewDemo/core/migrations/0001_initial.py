# Generated by Django 4.0.4 on 2022-06-13 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pquant', models.IntegerField()),
                ('pprice', models.IntegerField()),
            ],
        ),
    ]
