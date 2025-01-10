from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from blog.models import Blog

# Create your views here.
class BlogView(TemplateView):
    template_name = 'blogs.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all().order_by('-date')
        return context
class BlogDetailView(View):
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        context = {
            'blog': blog,
            'blogs': Blog.objects.all()
        }
        return render(request, 'singleBlogs.html', context=context)