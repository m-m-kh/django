# Generated by Django 5.0.2 on 2024-02-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('datatime_created', models.DateTimeField(auto_now_add=True)),
                ('datatime_modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('count', models.PositiveIntegerField()),
            ],
        ),
    ]
