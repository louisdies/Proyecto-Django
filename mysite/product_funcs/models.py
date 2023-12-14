from django.db import models

# Modelo de los productos.
class Product(models.model):
    name = models.CharFiel(max_length=50)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    base_cost_per_kilogram = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    #Método predeterminado de Django para guardar cálculo en base de datos.
    def save(self, *args, **kwargs):
        self.price = self.weight * self.base_cost_per_kilogram
        super().save(*args, **kwargs)
