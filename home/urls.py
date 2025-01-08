from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('repair/<str:device_id>', views.device_detail, name='repair')
]
