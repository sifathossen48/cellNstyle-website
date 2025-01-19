from django import forms

from Website_Settings.models import Store
from .models import DeviceProblem, DeviceSellImage, DeviceSell, Device, Brand, FranchiseContact, Model, Repair

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

from django import forms
from .models import Repair

class RepairForm(forms.ModelForm):
    problem = forms.ModelMultipleChoiceField(
        queryset=DeviceProblem.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # You can use this for a multi-checkbox field
        required=False  # Makes the problem field optional
    )
    class Meta:
        model = Repair
        fields = [
            'device', 'brand', 'model', 'problem', 'description',
            'serviceReceiveMethod', 'store', 'date', 'date2', 'time', 'streetAddress',
            'customerFirstName', 'customerLastName', 'customerEmail', 'customerPhone', 'termsAndConditions'
        ]
   


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     # Initializing field conditions based on serviceReceiveMethod
    #     self.fields['date'].disabled = True
    #     self.fields['date2'].disabled = True
    #     self.fields['store'].disabled = False
    #     self.fields['store'].queryset = Store.objects.all() 

    #     # Update field visibility based on the serviceReceiveMethod
    #     if self.instance and self.instance.serviceReceiveMethod:
    #         self.update_field_visibility()

    # def update_field_visibility(self):
    #     service_method = self.instance.serviceReceiveMethod

    #     # Enable/Disable fields based on serviceReceiveMethod
    #     if service_method == 'Visit Store':
    #         self.fields['date'].disabled = False
    #         self.fields['date2'].disabled = True
    #         self.fields['store'].disabled = False
    #         self.fields['streetAddress'].disabled = True
    #     elif service_method == 'Mail in':
    #         self.fields['date'].disabled = True
    #         self.fields['date2'].disabled = True
    #         self.fields['store'].disabled = True
    #         self.fields['streetAddress'].disabled = False
    #     elif service_method == 'Come to me':
    #         self.fields['date'].disabled = True
    #         self.fields['date2'].disabled = False
    #         self.fields['store'].disabled = True
    #         self.fields['streetAddress'].disabled = False

    # # Dynamically update the field visibility when `serviceReceiveMethod` changes
    # def clean(self):
    #     cleaned_data = super().clean()
    #     service_receive_method = cleaned_data.get('serviceReceiveMethod')

    #     if service_receive_method == 'Visit Store':
    #         if not cleaned_data.get('date'):
    #             self.add_error('date', 'Date is required for "Visit Store" service method.')
    #     elif service_receive_method == 'Mail in':
    #         if cleaned_data.get('date') or cleaned_data.get('date2'):
    #             self.add_error('date', 'Date should not be filled for "Mail in" service method.')
    #     elif service_receive_method == 'Come to me':
    #         if not cleaned_data.get('date2'):
    #             self.add_error('date2', 'Date2 is required for "Come to me" service method.')
        
    #     return cleaned_data