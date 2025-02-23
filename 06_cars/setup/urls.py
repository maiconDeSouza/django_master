from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cars import views as views_cars
from accounts import views as views_accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views_accounts.registier_view, name='register'),
    path('login/', views_accounts.login_view, name='login'),
    path('logout/', views_accounts.logout_view, name='logout'),
    path('', views_cars.cars_view, name='car_list'),
    path('new_car/', views_cars.new_car, name='new_car')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
