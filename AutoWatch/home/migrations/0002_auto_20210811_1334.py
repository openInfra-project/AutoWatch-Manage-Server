# Generated by Django 2.2.14 on 2021-08-11 04:34

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(storage=home.models.OverwriteStorage(), upload_to='', verbose_name='이미지'),
        ),
    ]