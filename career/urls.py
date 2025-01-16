from django.urls import path
from career import views


urlpatterns = [
    path('', views.career, name='career'),
]
