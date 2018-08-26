from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from fitways import views

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('', views.home, name='home'),
                  path('get_dates', views.get_dates, name='get_dates'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
