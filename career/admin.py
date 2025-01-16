from django.contrib import admin

from career.models import OpeningJob, JobApplication, JobCategory

# Register your models here.
admin.site.register(JobCategory)
admin.site.register(OpeningJob)
admin.site.register(JobApplication)