from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('repair/<str:device_slug>', views.device_detail, name='repair'),
    path('repair', views.repair_form_submit, name='repair_submit'),
    path('sell/', views.sell, name='device_submission_form'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('franchise/', views.franchise, name='franchise'),
    path('termsAndConditions/', views.TermsView.as_view(), name='terms'),
    path('privacyPolicy/', views.PrivacyView.as_view(), name='privacy'),
    path('products/', views.ProductView.as_view(), name='products'),
    path('search/', views.search_products, name='search_products'),
]
