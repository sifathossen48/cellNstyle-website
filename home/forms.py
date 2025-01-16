from django import forms
from .models import DeviceSell, Device, Brand, FranchiseContact, Model

class DeviceSellForm(forms.ModelForm):
    deviceImages = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    class Meta:
        model = DeviceSell
        fields = ['type', 'brand', 'model', 'description', 'customerFirstName', 'customerLastName', 'customerEmail', 'customerPhone', 'deviceImages']


 
class FranchiseContactForm(forms.ModelForm):
    class Meta:
        model = FranchiseContact
        fields = '__all__'     