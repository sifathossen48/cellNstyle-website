from django.urls import path
from django.conf.urls import handler404
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
    path('404/', views.custom_404_view, name='404'),
    # path('repair/', views.get_brand_name, name='repair_submit'),  # URL for the repair page
    path('get-models/', views.get_models, name='get_models'),
    path('get-brands/', views.get_brands, name='get_brands'),
]


handler404 = 'cellNstyle_website.views.custom_404_view'
