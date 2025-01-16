# Generated by Django 4.2 on 2025-01-16 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicesell',
            name='deviceImages',
        ),
        migrations.CreateModel(
            name='DeviceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='device_images/')),
                ('device_sell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.devicesell')),
            ],
        ),
    ]
