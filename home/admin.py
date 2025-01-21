from django.contrib import admin
from django.utils.html import format_html
from home.forms import RepairForm
from home.models import Brand, Device, DeviceSellImage, DeviceProblem, Features, FranchiseContact, FranchiseSections, Model, Product, ProductCategory, Repair, Slider, DeviceSell

# Register your models here.
admin.site.register(Slider)
admin.site.register(Device)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(DeviceProblem)
admin.site.register(FranchiseSections)
admin.site.register(Features)
admin.site.register(FranchiseContact)
admin.site.register(DeviceSell)
admin.site.register(DeviceSellImage)
admin.site.register(Repair)
admin.site.register(ProductCategory)
admin.site.register(Product)