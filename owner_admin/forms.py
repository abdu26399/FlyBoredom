from django import forms
from owner_admin.models import Offers


class AddOrEditOfferForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = '__all__'
        widgets = {'date_added': forms.DateInput(attrs={'hidden': True, 'readonly': True}),
                   'from_date': forms.DateInput(attrs={'type': 'date'}),
                   'to_date': forms.DateInput(attrs={'type': 'date'})}
