from django import forms
from .models import DeviceSellImage, DeviceSell, Device, Brand, FranchiseContact, Model

class DeviceSellForm(forms.ModelForm):
    class Meta:
        model = DeviceSell
        fields = "__all__"

class DeviceSellImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"multiple":True}))
    class Meta:
        model = DeviceSellImage
        fields = ['image']

class FranchiseContactForm(forms.ModelForm):
    class Meta:
        model = FranchiseContact
        fields = '__all__' 