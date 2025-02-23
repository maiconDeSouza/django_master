from django import forms
from django.core.exceptions import ValidationError
from .models import Car


# class CarsForms(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     factory_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageField()

#     def save(self):
#         car = Car(
#             model=self.cleaned_data['model'],
#             brand=self.cleaned_data['brand'],
#             factory_year=self.cleaned_data['factory_year'],
#             plate=self.cleaned_data['plate'],
#             value=self.cleaned_data['value'],
#             photo=self.cleaned_data['photo'],
#         )
#         car.save()
#         return car


class CarsForms(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 5000:
            self.add_error(
                'value', 'Não Aceitamos carros a baixo de 5 mil reais')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1930:
            self.add_error(
                'factory_year', 'Só Aceitamos carros fabricados acima de 1929')
