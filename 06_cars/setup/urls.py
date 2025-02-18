from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cars_view, name='car_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
