from django.contrib import admin

from home.models import Brand, Device, DeviceProblem, Model, Slider, DeviceSell

# Register your models here.
admin.site.register(Slider)
admin.site.register(Device)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(DeviceProblem)
admin.site.register(DeviceSell)

