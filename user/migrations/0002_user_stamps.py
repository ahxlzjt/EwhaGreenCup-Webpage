# Generated by Django 3.2.4 on 2024-10-30 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stamps',
            field=models.IntegerField(default=0),
        ),
    ]
