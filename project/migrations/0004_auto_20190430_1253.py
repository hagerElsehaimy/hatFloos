# Generated by Django 2.1 on 2019-04-30 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_featuredproject_feature_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]