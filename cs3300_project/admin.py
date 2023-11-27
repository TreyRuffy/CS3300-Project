from django.contrib import admin

# Register your models here.
from .models import Horse, BuyableHorse, Pedigree, Account
admin.site.register(Horse)
admin.site.register(BuyableHorse)
admin.site.register(Pedigree)
admin.site.register(Account)