from django.contrib import admin

from home.models import Brand, Device, Model, Slider

# Register your models here.
admin.site.register(Slider)
admin.site.register(Device)
admin.site.register(Brand)
admin.site.register(Model)

