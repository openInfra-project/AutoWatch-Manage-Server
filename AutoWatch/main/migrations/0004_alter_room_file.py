# Generated by Django 3.2.5 on 2021-08-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210730_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='file',
            field=models.FileField(default='NULL', upload_to='room', verbose_name='파일'),
        ),
    ]
