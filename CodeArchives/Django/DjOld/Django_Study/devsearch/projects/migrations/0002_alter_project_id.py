# Generated by Django 4.0.4 on 2022-06-05 03:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]