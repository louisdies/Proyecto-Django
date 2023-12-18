from django.contrib import admin
from .models import Product

#Permite mostrar al admin y modificar los campos de la instancia en la base de datos.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'weight', 'base_cost_per_kilogram', 'image', 'is_active', 'slug')	
    list_editable = ('weight', 'base_cost_per_kilogram', 'stock', 'image', 'is_active', 'slug')

#Registra el modelo en la base de datos.
admin.site.register(Product, ProductAdmin)