from django.db import models
from django.utils.text import slugify

# Modelo de los productos.
class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    base_cost_per_kilogram = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)
    
    #Método predeterminado de Django para guardar cálculo en base de datos.
    def save(self, *args, **kwargs):
        self.price = self.weight * self.base_cost_per_kilogram
        super().save(*args, **kwargs)

    #Genera slugs si el administrador no lo crea.
    def save(self, *args, **kwargs):
            if not self.slug:  # if slug wasn't provided, create one from the name
                self.slug = slugify(self.name)
            super(Product, self).save(*args, **kwargs)