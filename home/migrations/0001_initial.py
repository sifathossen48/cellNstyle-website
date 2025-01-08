# Generated by Django 4.2 on 2025-01-07 19:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(max_length=150)),
                ('subtitle', models.TextField()),
                ('image', models.ImageField(upload_to='slider/')),
                ('button_text', models.CharField(max_length=100)),
                ('button_link', models.CharField(max_length=200)),
                ('link_type', models.CharField(choices=[('url', 'External URL'), ('tel', 'Phone Link'), ('scroll', 'Scroll to Section')], default='url', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
