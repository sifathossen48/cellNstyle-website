from django.db import models

# Create your models here.
class WebsiteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    site_logo = models.ImageField(upload_to='website_settings')
    site_favicon = models.ImageField(upload_to='website_settings')
    facebook_url = models.URLField()
    whatsApp_number = models.CharField(max_length=20)
    email = models.EmailField()
    youtube_url = models.URLField()
    def __str__(self):
        return "Website Settings"

class Store(models.Model):
    area = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    google_map_link = models.URLField(max_length=200)
    google_map_iframe_link = models.TextField()
    def __str__(self):
        return self.area