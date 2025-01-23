from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from Website_Settings.models import Store
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Slider(models.Model):
    LINK_TYPE_CHOICES = [
        ('url', 'External URL'),
        ('tel', 'Phone Link'),
        ('scroll', 'Scroll to Section'),
    ]
    title = RichTextField(max_length=500)
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
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Automatically generate slug from name
        super().save(*args, **kwargs)
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

class Repair(models.Model):
    SERVICE_RECEIVE_METHOD_CHOICES = [
        ('visitStore', 'visitStore'),
        ('mail', 'mail'),
        ('comeToMe', 'comeToMe'),
    ]
    TIME_CHOICES = [
        ('12am-2am', '12am-2am'),
        ('2am-4am', '2am-4am'),
        ('4am-6am', '4am-6am'),
        ('6am-8am', '6am-8am'),
        ('8am-10am', '8am-10am'),
        ('10am-12am', '10am-12am'),
    ]
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True)
    problem = models.ManyToManyField(DeviceProblem)
    description = models.TextField(null=True, blank=True)
    serviceReceiveMethod = models.CharField(max_length=50,choices=SERVICE_RECEIVE_METHOD_CHOICES)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    date = models.CharField(max_length=50,null=True, blank=True)
    date2 = models.CharField(max_length=50,null=True, blank=True)
    time = models.CharField(max_length=20,choices=TIME_CHOICES,null=True, blank=True)
    streetAddress = models.CharField(max_length=200,null=True, blank=True)
    customerFirstName = models.CharField(max_length=100)
    customerLastName = models.CharField(max_length=100)
    customerEmail = models.EmailField()
    customerPhone = models.CharField(max_length=20)
    termsAndConditions = models.BooleanField(default=False)
    
    

    def __str__(self):
        return f"{self.customerFirstName} {self.customerLastName} wants repair for {self.device} | {self.brand} | {self.model}"
    def get_problems(self):
        return ", ".join([problem.problem for problem in self.problem.all()])

    
    def clean(self):
        # Conditional logic based on serviceReceiveMethod
        if self.serviceReceiveMethod == 'visitStore':
            if not self.store:
                raise ValidationError("Store is required when 'Visit Store' is selected.")
            if self.streetAddress:
                raise ValidationError("Street Address should be empty when 'Visit Store' is selected.")
            if not self.date:
                raise ValidationError("Date is required when 'Visit Store' is selected.")
            if self.date2:
                raise ValidationError("Date2 should be empty when 'Visit Store' is selected.")
        elif self.serviceReceiveMethod == 'mail':
            if self.date or self.date2 or self.time:
                raise ValidationError("Date and Time should be empty when 'Mail in' is selected.")
            if not self.streetAddress:
                raise ValidationError("Street Address is required when 'Mail in' is selected.")
            if self.store:
                raise ValidationError("Store should be empty when 'Mail in' is selected.")
        elif self.serviceReceiveMethod == 'comeToMe':
            if not self.streetAddress:
                raise ValidationError("Street Address is required when 'Come to me' is selected.")
            if self.store:
                raise ValidationError("Store should be empty when 'Come to me' is selected.")
            if not self.date2:
                    raise ValidationError("Date2 is required when 'Come to me' is selected.")
            if self.date:
                raise ValidationError("Date should be empty when 'Come to me' is selected.")

class ProductCategory(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    previous_price = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(194)], blank=True, null=True)
    original_price = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(194)])
    def __str__(self):
        return self.title