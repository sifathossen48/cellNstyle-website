# Generated by Django 4.2 on 2025-01-17 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website_Settings', '0004_store_country_code'),
        ('home', '0004_repair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Website_Settings.store'),
        ),
    ]
