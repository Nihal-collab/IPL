# Generated by Django 5.2.3 on 2025-06-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ipl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=100)),
                ('captain', models.CharField(max_length=100)),
                ('cups', models.IntegerField()),
            ],
        ),
    ]
