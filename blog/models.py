from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/')
    description = RichTextField(config_name='all')
    description2 = RichTextField(config_name='all',blank=True,null=True)
    video_link = models.CharField(max_length=1000,blank=True,null=True)
    date = models.DateField()

    def __str__(self):
        return self.title