from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from datetime import datetime, timedelta
from blog.models import Blog
from home.forms import DeviceSellForm, FranchiseContactForm
from home.models import Brand, Device, DeviceProblem, DeviceSell, FranchiseSections, Model, Slider
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        context['blogs'] = Blog.objects.all().order_by('-date')[:3]
        
        return context
def device_detail(request, device_id):
    
    device = get_object_or_404(Device, id=device_id)
    brand = Brand.objects.filter(device=device)
    device_problems = DeviceProblem.objects.all()
    has_brands = brand.exists()
    today = datetime.today()

    # Generate the next 7 days with day and date
    next_7_days = []
    for i in range(7):
        day_date = today + timedelta(days=i)
        day_of_week = day_date.strftime("%a")
        date = day_date.strftime("%d %B")  
        next_7_days.append({'day': day_of_week, 'date': date})
    
 
        
    context = {
      
        'device': device,
        'brand': brand,
        'has_brands': has_brands,
        'device_problems': device_problems,
        'next_7_days': next_7_days,
        }
    return render(request, 'repair.html', context=context)



def sell(request):
    success_message = None
    brands = Brand.objects.all()
    models = Model.objects.all()

    if request.method == "POST":
        form = DeviceSellForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Form submitted successfully!") 
        else:
            messages.error(request,'Invalid! Please try again.')

            # Optionally, redirect to another page after form submission to avoid re-submission
            return redirect('device_submission_form')  # Redirect to the same form or another page

    else:
        form = DeviceSellForm()

    # Pass the form and the success message (if any) to the template
    return render(request, 'sell.html', {
        'form': form,
        'brands': brands,
        'models': models,
        'success_message': success_message,
    })
class ContactView(TemplateView):
    template_name = 'contact.html'
    

def franchise(request):
    section = FranchiseSections.objects.all()
    if request.method == 'POST':
        form = FranchiseContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Your submission was successful!')
        else:
            messages.error(request, 'Invalid! Please try again.')
    else:
        form = FranchiseContactForm()
    return render(request, 'franchise.html',{ 'section': section, 'form': form})