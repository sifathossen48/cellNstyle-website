from django.urls import path
from career import views


urlpatterns = [
    path('career/', views.career, name='career'),
]
