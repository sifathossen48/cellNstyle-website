from django import forms
from .models import DeviceSell, Device, Brand, FranchiseContact, Model

class DeviceSellForm(forms.ModelForm):
    class Meta:
        model = DeviceSell
        fields = ['type', 'brand', 'model', 'description', 'customerFirstName', 'customerLastName',  'customerEmail', 'customerPhone', 'deviceImages']


    def clean_customerEmail(self):
        email = self.cleaned_data.get('customerEmail')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email
    def clean_deviceImages(self):
        deviceImage = self.cleaned_data.get('deviceImages')
        if not deviceImage.name.endswith('.jpg'):
            raise forms.ValidationError("Only JPG files are allowed.")
        return deviceImage
class FranchiseContactForm(forms.ModelForm):
    class Meta:
        model = FranchiseContact
        fields = '__all__'     