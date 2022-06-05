from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *

class DelivView(CreateView):
    form_class = DelivForm
    template_name = 'dform/index.html'
    context_object_name = 'form'
    success_url = reverse_lazy('deliveryform')


    def get_request(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        delivery_address_form = DelivAddressFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  delivery_address_form=delivery_address_form,
                                  )
        )

    def post_request(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        delivery_address_form = DelivAddressFormSet(self.request.POST, self.request.FILES, instance=form.instance)
        if form.is_valid() and delivery_address_form.is_valid():
            return self.form_valid(form, delivery_address_form)
        else:
            return self.form_invalid(form, delivery_address_form)

    def form_valid(self, form, delivery_address_form):
        self.object = form.save(commit=False)
        # pre-processing for Assignment instance here...
        self.object.save()

        # saving AssignmentQuestion Instances
        delivery_address = delivery_address_form.save(commit=False)
        for aq in delivery_address:
            #  change the AssignmentQuestion instance values here
            #  aq.some_field = some_value
            aq.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, delivery_address_form):
        return self.render_to_response(
            self.get_context_data(form=form, deliveryaddress_form=delivery_address_form))