# Generated by Django 3.1.4 on 2021-05-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subheading', models.CharField(max_length=255, verbose_name='subheading')),
                ('model_for_car', models.CharField(max_length=255, verbose_name='Model for car')),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('mileage', models.CharField(max_length=255, verbose_name='Mileage')),
                ('transmission', models.CharField(max_length=255, verbose_name='Transmission')),
                ('fuel', models.CharField(max_length=255, verbose_name='Fuel')),
                ('seats', models.CharField(max_length=255, verbose_name='Seats')),
                ('luggage', models.CharField(max_length=255, verbose_name='Luggage')),
                ('airconditions', models.BooleanField(verbose_name='airconditions')),
                ('child_seat', models.BooleanField(verbose_name='child seat')),
                ('GPS', models.BooleanField(verbose_name='GPS')),
                ('music', models.BooleanField(verbose_name='music')),
                ('seat_belt', models.BooleanField(verbose_name='seat belt')),
                ('sleeping_bed', models.BooleanField(verbose_name='sleeping bed')),
                ('water', models.BooleanField(verbose_name='water')),
                ('bluetooth', models.BooleanField(verbose_name='bluetooth')),
                ('onboard_computer', models.BooleanField(verbose_name='onboard computer')),
                ('audio_input', models.BooleanField(verbose_name='audio input')),
                ('long_term_tripl', models.BooleanField(verbose_name='long term tripl')),
                ('car_kit', models.BooleanField(verbose_name='car kit')),
                ('remote_central_locking', models.BooleanField(verbose_name='remote central locking')),
                ('climate_control', models.BooleanField(verbose_name='climate control')),
                ('description', models.TextField(null=True, verbose_name='description')),
                ('cost_hour', models.CharField(max_length=255, verbose_name='cost_hour')),
                ('cost_day', models.CharField(max_length=255, verbose_name='cost_day')),
                ('cost_mounth', models.CharField(max_length=255, verbose_name='cost_mounth')),
            ],
        ),
    ]