# Generated by Django 3.1 on 2020-08-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('title', models.CharField(max_length=70)),
                ('body', models.TextField()),
            ],
        ),
    ]
