from django.contrib import admin
from .models import Car, Brand, CarInventory

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')


class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('car_count', 'cars_value', 'created_at')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarInventory, CarInventoryAdmin)
