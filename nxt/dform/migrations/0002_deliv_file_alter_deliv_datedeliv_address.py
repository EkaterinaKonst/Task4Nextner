# Generated by Django 4.0.5 on 2022-06-05 19:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliv',
            name='File',
            field=models.FileField(default=django.utils.timezone.now, upload_to='files/', verbose_name='File address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliv',
            name='DateDeliv',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AddressDeliv', models.CharField(max_length=200, verbose_name='Address')),
                ('Delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dform.deliv', verbose_name='Order')),
            ],
        ),
    ]
