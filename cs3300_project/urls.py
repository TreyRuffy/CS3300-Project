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
    path('horse/add', views.add_horse, name='add_horse'),
    path('horse/edit/<int:horse_id>', views.edit_horse, name='edit_horse'),
    path('horse/delete/<int:horse_id>', views.delete_horse, name='delete_horse'),
    path('pedigree/<int:horse_id>', views.pedigree, name='pedigree'),
    path('login', views.loginPage, name='login'),
    path('account', views.account, name='account'),
    path('logout', views.logoutPage, name='logout'),
    path('register', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)