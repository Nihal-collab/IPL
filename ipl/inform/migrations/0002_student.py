# Generated by Django 5.2.3 on 2025-06-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
    ]
