from django.shortcuts import render
from django.contrib import messages
from career.forms import JobApplicationForm
from career.models import OpeningJob

# Create your views here.
def career(request):
    jobs = OpeningJob.objects.filter(is_active=True)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_id = request.POST.get('job')
            if job_id:
                job = OpeningJob.objects.filter(id=job_id).first()
                if job:
                    application = form.save(commit=False)
                    application.job = job
                    application.save()
                    messages.success(request, 'Your application has been submitted successfully.')
                else:
                    messages.error(request, 'Selected job does not exist.')
            else:
                messages.error(request, 'No job selected.')
        else:
            messages.error(request, 'Form submission failed.')
            print(form.errors)  # Debugging: Log errors

    else:
        form = JobApplicationForm()

    return render(request, 'career.html', {'jobs': jobs, 'form': form})
