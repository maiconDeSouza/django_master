from django import forms
from .models import Car


# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     image = forms.ImageField()

#     def save(self):
#         model = self.cleaned_data['model']
#         brand = self.cleaned_data['brand']
#         factory_year = self.cleaned_data['factory_year']
#         model_year = self.cleaned_data['model_year']
#         plate = self.cleaned_data['plate']
#         value = self.cleaned_data['value']
#         image = self.cleaned_data['image']

#         new_car = Car(model=model, brand=brand, factory_year=factory_year,
#                       model_year=model_year, plate=plate, value=value, image=image)

#         new_car.save()
#         return new_car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 2000:
            self.add_error(
                'value', 'Valor mínimo do carro deve ser de R$2.000,00')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1950:
            self.add_error(
                'factory_year', 'Não é aceito carros anteriores a 1950')
        return factory_year
