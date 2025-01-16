from django import forms

from career.models import JobApplication, OpeningJob

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message', 'cv']
     