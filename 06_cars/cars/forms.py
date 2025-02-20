from django import forms
from .models import Brand

# model = models.CharField(max_length=200)
#     brand = models.ForeignKey(
#         Brand, on_delete=models.PROTECT, related_name='car_brand')
#     factory_year = models.IntegerField()
#     plate = models.CharField(max_length=10, blank=True, null=True)
#     value = models.FloatField(blank=True, null=True)
#     photo = models.ImageField(upload_to='cars/', blank=True, null=True)


class CarsForms(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()
