# Generated by Django 2.2.14 on 2021-08-10 07:50

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_user_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='face-recognition.png', storage=home.models.OverwriteStorage(), upload_to='', verbose_name='이미지'),
        ),
    ]
