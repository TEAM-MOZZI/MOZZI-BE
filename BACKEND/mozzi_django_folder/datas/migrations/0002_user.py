# Generated by Django 4.1.13 on 2024-03-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_code', models.CharField(max_length=20)),
                ('user_nickname', models.CharField(max_length=20)),
                ('user_register_date', models.DateTimeField()),
                ('user_isvegan', models.BooleanField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
