from django.forms import ModelForm, inlineformset_factory
from .models import *

class DelivForm(ModelForm):
    class Meta:
        model = Deliv
        fields = '__all__'

DelivAddressFormSet = inlineformset_factory(Deliv, Address, fields=['AddressDeliv'], can_delete=False, extra=1)