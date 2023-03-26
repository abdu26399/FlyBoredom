from django import forms
from owner_admin.models import Offers


class AddOrEditOfferForm(forms.ModelForm):
    def is_valid(self):
        valid = super(AddOrEditOfferForm, self).is_valid()
        if not valid:
            return valid
        from_date = self.cleaned_data['from_date']
        to_date = self.cleaned_data['to_date']
        if from_date > to_date:
            self.add_error('to_date', 'To date must be after from date.')
            return False
        return True
        
    class Meta:
        model = Offers
        fields = '__all__'
        widgets = {'date_added': forms.DateInput(attrs={'hidden': True, 'readonly': True}),
                   'from_date': forms.DateInput(attrs={'type': 'date'}),
                   'to_date': forms.DateInput(attrs={'type': 'date'})}
