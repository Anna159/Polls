# Generated by Django 2.2.4 on 2019-09-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_tag_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='question',
            field=models.ManyToManyField(to='polls.Question'),
        ),
    ]
