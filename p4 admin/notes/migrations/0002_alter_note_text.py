# Generated by Django 5.0.2 on 2024-02-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(),
        ),
    ]
