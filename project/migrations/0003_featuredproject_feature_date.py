# Generated by Django 2.1 on 2019-04-29 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_featuredproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredproject',
            name='feature_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
