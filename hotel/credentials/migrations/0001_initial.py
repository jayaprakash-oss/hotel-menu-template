# Generated by Django 4.1.7 on 2023-04-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30)),
                ('Lastname', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=13)),
                ('Password', models.CharField(default='NA', max_length=50)),
                ('Email', models.CharField(default='NA', max_length=40)),
            ],
        ),
    ]
