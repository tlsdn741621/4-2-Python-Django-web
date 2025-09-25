from django.contrib import admin

# Register your models here.
from burgers.models import Burger

@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass