# Generated by Django 3.2.5 on 2021-08-05 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_user_registerd_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='room',
        ),
    ]