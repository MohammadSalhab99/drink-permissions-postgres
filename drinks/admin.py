from django.contrib import admin
from .models import Drink


@admin.register(Drink)
class AdminDrink(admin.ModelAdmin):

    list_display= ["name","description", "customer"]