# Generated by Django 3.0.8 on 2020-08-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_room_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='beds',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
