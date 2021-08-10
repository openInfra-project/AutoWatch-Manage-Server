# Generated by Django 3.2.5 on 2021-08-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_analytics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analytics',
            name='username',
        ),
        migrations.AddField(
            model_name='analytics',
            name='email',
            field=models.EmailField(default='NULL', max_length=128, verbose_name='아이디'),
        ),
    ]