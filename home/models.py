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

class DeviceProblem(models.Model):
    problem = models.CharField(max_length=100)
    def __str__(self):
        return self.problem

class DeviceSell(models.Model):
    type = models.ForeignKey(Device, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE) 
    description = models.TextField()
    customerFirstName = models.CharField(max_length=100)
    customerLastName = models.CharField(max_length=100)
    customerEmail = models.EmailField()
    customerPhone = models.CharField(max_length=15)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.customerFirstName} {self.customerLastName} - {self.type} {self.brand} {self.model}"
class DeviceSellImage(models.Model):
    device_sell = models.ForeignKey(DeviceSell, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='device_images/')
    def __str__(self):
        return f"{self.device_sell.customerFirstName} {self.device_sell.customerLastName}'s device image "


class FranchiseSections(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    @property
    def get_features(self):
        return self.features.all()
    
class Features(models.Model):
    section = models.ForeignKey(FranchiseSections, on_delete=models.CASCADE,  related_name="features")
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class FranchiseContact(models.Model):
    franchiseApplicantFirstName = models.CharField(max_length=100)
    franchiseApplicantLastName = models.CharField(max_length=100)
    franchiseApplicantEmail = models.EmailField(unique=True)
    franchiseApplicantPhone = models.CharField(max_length=15)
    franchiseApplicantStreetAddress = models.CharField(max_length=200)
    aboutFranchiseApplicant = models.TextField()
    def __str__(self):
        return self.franchiseApplicantFirstName + " " + self.franchiseApplicantLastName