from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # path function defines a url pattern
    # '' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name = 'index' parameter is to dynamically create url
    # example in html <a h
    path('', views.index, name='index'),
    path('horse/<int:horse_id>', views.horse, name='horse'),
    path('horse/edit/<int:horse_id>', views.edit_horse, name='edit_horse'),
    path('pedigree/<int:horse_id>', views.pedigree, name='pedigree'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)