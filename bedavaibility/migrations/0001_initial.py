# Generated by Django 3.2.3 on 2021-05-21 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=12)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospitals', to='bedavaibility.city')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('hospital', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bedavaibility.hospital')),
                ('bed_availability', models.IntegerField(default=0)),
                ('bed_total', models.IntegerField(default=0)),
                ('oxygen_availability', models.IntegerField(default=0)),
                ('oxygen_total', models.IntegerField(default=0)),
                ('ventilator_avvailibility', models.IntegerField(default=0)),
                ('ventilator_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='bedavaibility.state'),
        ),
    ]
