from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import *
from .models import *

class DelivView(TemplateView):
    template_name = 'dform/index.html'
    success_url = reverse_lazy('deliveryform')


    def get(self, *args, **kwargs):
        formset = DelivAddressFormSet(queryset=Deliv.objects.none())
        return self.render_to_response({'d_formset': formset})

    def post(self, *args, **kwargs):
        formset = DelivAddressFormSet(data=self.request.POST)
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy('deliveryform'))
        return self.render_to_response({'d_formset': formset})