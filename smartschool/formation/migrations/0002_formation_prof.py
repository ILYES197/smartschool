# Generated by Django 5.0.6 on 2024-06-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='prof',
            field=models.CharField(default='', max_length=200),
        ),
    ]