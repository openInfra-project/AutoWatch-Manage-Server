# Generated by Django 3.2.5 on 2021-08-09 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210809_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytics',
            name='make_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성 날짜'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analytics',
            name='time',
            field=models.IntegerField(default=0, verbose_name='학습 시간'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='make_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜'),
        ),
    ]