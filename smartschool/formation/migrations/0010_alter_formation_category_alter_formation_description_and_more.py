# Generated by Django 4.2.7 on 2025-02-10 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formation', '0009_alter_formation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='category',
            field=models.CharField(choices=[('ابتدائي', 'Primaire'), ('متوسط', 'Moyen'), ('ثانوي', 'Secondaire'), ('جامعة', 'Universitaire'), ('لغات أجنبية', 'Langues Etrangeres'), ('دورات متنوعة', 'Divers')], max_length=60),
        ),
        migrations.AlterField(
            model_name='formation',
            name='description',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='formation',
            name='name',
            field=models.CharField(default='', max_length=900),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
