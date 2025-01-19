from Website_Settings.models import PrivacyPolicy, Store, TermsAndConditions, WebsiteSettings

def common(request):
    web = WebsiteSettings.objects.last()
    store = Store.objects.all()
    terms = TermsAndConditions.objects.last()
    privacy = PrivacyPolicy.objects.last()
    return {'web': web, 'store': store, 'terms':terms, 'privacy':privacy}