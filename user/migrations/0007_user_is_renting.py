# Generated by Django 5.1.2 on 2024-11-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rentalcode_used_by_returncode_used_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_renting',
            field=models.BooleanField(default=False),
        ),
    ]
