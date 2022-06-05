from django.urls import path

from .views import *

urlpatterns = [
    path('', DelivView.as_view(), name='deliveryform'),
]