# Generated by Django 3.2.3 on 2021-05-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedavaibility', '0003_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='available',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='availability',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]