from itertools import product

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from store.views import home, contact

urlpatterns = [
    path('', home, name = 'name'),
    path('contact', contact,name='contact'),
    path('products/<slug>/',product,name='products'),

]+static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)