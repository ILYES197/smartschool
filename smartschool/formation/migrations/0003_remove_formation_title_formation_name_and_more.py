# Generated by Django 5.0.6 on 2024-06-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0002_formation_prof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='title',
        ),
        migrations.AddField(
            model_name='formation',
            name='Name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='formation',
            name='category',
            field=models.CharField(default='', max_length=40),
        ),
    ]