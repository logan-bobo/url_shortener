# Generated by Django 3.2.12 on 2022-11-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=10, unique=True)),
                ('origin_link', models.CharField(max_length=200)),
            ],
        ),
    ]
