# Generated by Django 4.1.13 on 2024-03-21 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('category_pic', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=30)),
                ('food_recipe', models.CharField(max_length=255)),
                ('food_views', models.IntegerField()),
                ('food_pic', models.CharField(max_length=200)),
                ('food_salty_rate', models.FloatField()),
                ('food_sweet_rate', models.FloatField()),
                ('food_bitter_rate', models.FloatField()),
                ('food_sour_rate', models.FloatField()),
                ('food_umami_rate', models.FloatField()),
                ('food_spicy_rate', models.FloatField()),
                ('food_category', models.CharField(max_length=5)),
                ('food_today_views', models.IntegerField()),
                ('food_category_count', models.IntegerField()),
            ],
        ),
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
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=50, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datas.category')),
            ],
        ),
    ]
