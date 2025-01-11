from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('repair/<str:device_id>', views.device_detail, name='repair'),
    path('sell/', views.sell, name='device_submission_form'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
