# Generated by Django 3.0.3 on 2020-03-01 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20190917_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]