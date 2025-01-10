from django.urls import path

from . import views
urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('<int:blog_id>/', views.BlogDetailView.as_view(), name='blog-detail'),
]
