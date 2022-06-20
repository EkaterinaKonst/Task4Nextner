from django.db import models

class Deliv(models.Model):
    NameGoods=models.CharField(max_length=255)
    TypeGoods=models.CharField(max_length=255)
    DateDeliv=models.DateField(auto_now=False, blank=True, null=True)
    File = models.FileField(verbose_name='File address', upload_to='files/', blank=True, null=True)


    def __str__(self):
        return self.NameGoods


class Address(models.Model):
    AddressDeliv = models.CharField(max_length=200, verbose_name='Address')
    Delivery = models.ForeignKey(Deliv, models.CASCADE, verbose_name='Order')
