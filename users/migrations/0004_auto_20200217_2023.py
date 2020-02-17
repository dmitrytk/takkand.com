# Generated by Django 3.0.1 on 2020-02-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_photos', verbose_name='Profile photo'),
        ),
    ]
