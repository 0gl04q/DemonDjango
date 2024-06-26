# Generated by Django 5.0.4 on 2024-04-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPUInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('cpu', models.FloatField()),
            ],
            options={
                'ordering': ('-time',),
                'indexes': [models.Index(fields=['time'], name='time_idx')],
            },
        ),
    ]
