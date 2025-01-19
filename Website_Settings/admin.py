from django.contrib import admin
from Website_Settings.models import PrivacyPolicy, Store, TermsAndConditions, WebsiteSettings

# Register your models here.
admin.site.register(WebsiteSettings)
admin.site.register(Store)
admin.site.register(TermsAndConditions)
admin.site.register(PrivacyPolicy)