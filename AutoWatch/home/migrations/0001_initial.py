# Generated by Django 3.2.5 on 2021-07-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registerd_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('email', models.EmailField(max_length=128, verbose_name='이메일')),
            ],
            options={
                'verbose_name': '사용자 명단',
                'verbose_name_plural': '사용자 명단',
                'db_table': 'hasik_user',
            },
        ),
    ]
