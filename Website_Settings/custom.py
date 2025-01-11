from Website_Settings.models import Store, WebsiteSettings

def common(request):
    web = WebsiteSettings.objects.first()
    store = Store.objects.all()
    return {'web': web, 'store': store}