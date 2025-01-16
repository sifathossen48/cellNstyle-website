from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class JobCategory(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class OpeningJob(models.Model):
    WORK_TYPE_CHOICES = [
        ('Onsite', 'Onsite'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
    ]

    EMPLOYMENT_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    ]

    title = models.CharField(max_length=255)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    responsibilities = RichTextField(config_name='all')
    requirements = RichTextField(config_name='all')
    posted_date = models.DateField(auto_now=True)  # Automatically sets the current date
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField(blank=True) 
    cv = models.FileField(upload_to='resumes/')
    job = models.ForeignKey(OpeningJob, on_delete=models.CASCADE)
    applied_at = models.DateField(auto_now=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job.title}"
