# Generated by Django 4.0.5 on 2022-06-25 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profiles/profile.jpg', null=True, upload_to='profiles/'),
        ),
    ]
