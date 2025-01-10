from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import TemplateView

from blog.models import Blog
from home.models import Brand, Device, Model, Slider
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
    has_brands = brand.exists()
 
        
    context = {
      
        'device': device,
        'brand': brand,
        'has_brands': has_brands,
        }
    return render(request, 'repair.html', context=context)
