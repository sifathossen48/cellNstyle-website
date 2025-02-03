def device(request):
    from home.models import Device
    devices = Device.objects.all().order_by('si_no')
    return {'devices': devices}