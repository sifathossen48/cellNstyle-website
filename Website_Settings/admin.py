from django.contrib import admin

from Website_Settings.models import Store, WebsiteSettings

# Register your models here.
admin.site.register(WebsiteSettings)
admin.site.register(Store)
