# Generated by Django 3.2.4 on 2021-06-09 15:28

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
                ('name', models.CharField(max_length=45)),
                ('account', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=80)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
