from django.forms import modelformset_factory
from .models import *

DelivAddressFormSet = modelformset_factory(
    Deliv, fields=("NameGoods", "TypeGoods","DateDeliv","File"), extra=1)
