# Generated by Django 4.2.7 on 2024-07-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_order_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
