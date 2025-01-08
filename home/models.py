from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags
# Create your models here.
class Slider(models.Model):
    LINK_TYPE_CHOICES = [
        ('url', 'External URL'),
        ('tel', 'Phone Link'),
        ('scroll', 'Scroll to Section'),
    ]
    title = RichTextField(max_length=150)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='slider/')
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=200) 
    link_type = models.CharField(max_length=10, choices=LINK_TYPE_CHOICES, default='url')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def clean_title(self):
        return strip_tags(self.title)

    def __str__(self):
        return self.clean_title()
class Device(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='devices/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def brands(self):
        return self.brand_set.all()
    
class Brand(models.Model):
    name = models.CharField(max_length=25)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.device.name})"
    def get_models(self):
        """Returns all models associated with this brand."""
        return self.model_set.all()
    
class Model(models.Model):
    name = models.CharField(max_length=25)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.brand.name})"