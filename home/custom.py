def device(request):
    from home.models import Device
    devices = Device.objects.all()
    return {'devices': devices}