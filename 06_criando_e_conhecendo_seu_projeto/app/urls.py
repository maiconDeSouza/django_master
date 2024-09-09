from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import home_cars_view, new_car_view
from accounts.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', home_cars_view, name="cars_list"),
    path('new_car/', new_car_view, name='new_car'),
    path('register/', register_view, name="register_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
