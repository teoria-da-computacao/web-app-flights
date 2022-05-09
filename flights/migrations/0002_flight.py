# Generated by Django 4.0.4 on 2022-05-09 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flights.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='flights.airport')),
            ],
        ),
    ]