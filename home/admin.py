from django.contrib import admin
from django.utils.html import format_html
from home.models import Brand, Device, DeviceProblem, Features, FranchiseContact, FranchiseSections, Model, Slider, DeviceSell

# Register your models here.
admin.site.register(Slider)
admin.site.register(Device)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(DeviceProblem)

admin.site.register(FranchiseSections)
admin.site.register(Features)
admin.site.register(FranchiseContact)

class DeviceSellAdmin(admin.ModelAdmin):
    list_display = ('type', 'brand', 'model', 'description', 'customerFirstName', 'customerLastName', 'customerEmail', 'customerPhone', 'deviceImages', 'submitted_at', )
admin.site.register(DeviceSell, DeviceSellAdmin)