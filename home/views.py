from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from django.conf import settings
import os

from datetime import datetime, timedelta
from Website_Settings.models import Store
from blog.models import Blog
from home.forms import DeviceSellForm, FranchiseContactForm, RepairForm
from home.models import Brand, Device, DeviceSellImage, DeviceProblem, DeviceSell, FranchiseSections, Model, Product, ProductCategory, Slider
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        context['blogs'] = Blog.objects.all().order_by('-date')[:3]
        context['categories'] = ProductCategory.objects.all()
        context['products'] = Product.objects.all()
        return context
def device_detail(request, device_slug): 
    device = get_object_or_404(Device, slug=device_slug)
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
@csrf_exempt  # Only use this if not using `csrf_token` in frontend
def repair_form_submit(request):
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            repair_instance = form.save(commit=False)
            # Additional logic: set default store if needed.
            if repair_instance.serviceReceiveMethod == 'Visit Store' and not repair_instance.store:
                repair_instance.store = Store.objects.first()
            
            repair_instance.save()
            selected_problems = form.cleaned_data.get('problem')
            if selected_problems:
                repair_instance.problem.set(selected_problems)
            repair_instance.save()
            messages.success(request, "Form Submitted Successfully")
        else:
            messages.error(request, "Invalid! Please Try Again.")
    else:
        form = RepairForm()

    # Build the dynamic selector data:
    brands = Brand.objects.all()
    models_by_brand = {}
    for brand in brands:
        # Using the related name 'models' from the DeviceModel foreign key to DeviceBrand
        models_by_brand[brand.name] = list(brand.models.values_list('name', flat=True))
    
    context = {
        'form': form,
        'brands': brands,
        'models_by_brand': models_by_brand,
    }
    return render(request, 'repair.html', context)



def sell(request):
    brands = Brand.objects.all()
    models = Model.objects.all()
    devices = Device.objects.all()

    if request.method == "POST":
        form = DeviceSellForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')  # Get the list of uploaded files

        if len(files) > 4:
            messages.error(request, 'Invalid! You can upload a maximum of 4 images.')
        else:
                # Validate image formats
            valid_extensions = ['.jpg', '.jpeg', '.png']
            invalid_files = [
                file.name for file in files
                if os.path.splitext(file.name)[1].lower() not in valid_extensions
            ]

            if invalid_files:
                messages.error(request,f"Invalid file format(s): {', '.join(invalid_files)}. Only JPG and PNG files are allowed.")
            elif form.is_valid():
                device_sell = form.save()
                # Save each image to the related model
                for file in files:
                    DeviceSellImage.objects.create(device_sell=device_sell, image=file)
                messages.success(request, "Form submitted successfully!")
            else:
                messages.error(request, 'Invalid! Please try again.')
    else:
        form = DeviceSellForm()

    return render(request, 'sell.html', {
        'form': form,
        'brands': brands,
        'models': models,
        'devices': devices,
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

class TermsView(TemplateView):
    template_name = 'termsConditions.html'

class PrivacyView(TemplateView):
    template_name = 'privacyPolicy.html'

class ProductView(TemplateView):
    template_name = 'products.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['products'] = Product.objects.all()
        return context
def search_products(request):
    query = request.GET.get('search', '')
    products = Product.objects.filter(title__icontains=query) if query else []
    return ({'products': products, 'query': query})

def custom_404_view(request, exception):
    return render(request, 'error.html', status=404)


def get_brands(request):
    device_id = request.GET.get('device_id')
    brands = Brand.objects.filter(device_id=device_id).values('id','name')
    return JsonResponse(list(brands), safe=False)

def get_models(request):
    brand_id = request.GET.get('brand_id')
    models = Model.objects.filter(brand_id=brand_id).values('id', 'name')
    return JsonResponse(list(models), safe=False)