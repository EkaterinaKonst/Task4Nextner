from django.db import models

class Deliv(models.Model):
    NameGoods=models.CharField(max_length=255)
    TypeGoods=models.CharField(max_length=255)
    DateDeliv=models.DateField(auto_now=False)
    File = models.FileField(verbose_name='File address', upload_to='files/')

    def get_absolute_url(self):
        return '/success/'

    def __str__(self):
        return self.name


class Address(models.Model):
    AddressDeliv = models.CharField(max_length=200, verbose_name='Address')
    Delivery = models.ForeignKey(Deliv, models.CASCADE, verbose_name='Order')
