# Generated by Django 5.0.2 on 2024-03-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]