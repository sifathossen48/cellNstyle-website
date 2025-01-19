# Generated by Django 4.2 on 2025-01-17 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website_Settings', '0004_store_country_code'),
        ('home', '0003_rename_deviceimage_devicesellimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('serviceReceiveMethod', models.CharField(choices=[('Visit Store', 'Visit Store'), ('Mail in', 'Mail in'), ('Come to me', 'Come to me')], default='Visit Store', max_length=50)),
                ('date', models.CharField(max_length=50, null=True)),
                ('date2', models.CharField(max_length=50, null=True)),
                ('time', models.CharField(choices=[('12am-2am', '12am-2am'), ('2am-4am', '2am-4am'), ('4am-6am', '4am-6am'), ('6am-8am', '6am-8am'), ('8am-10am', '8am-10am'), ('10am-12am', '10am-12am')], max_length=20)),
                ('streetAddress', models.CharField(max_length=200)),
                ('customerFirstName', models.CharField(max_length=100)),
                ('customerLastName', models.CharField(max_length=100)),
                ('customerEmail', models.EmailField(max_length=254)),
                ('customerPhone', models.CharField(max_length=20)),
                ('termsAndConditions', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.brand')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.device')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.model')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.deviceproblem')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Website_Settings.store')),
            ],
        ),
    ]
