from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class libro (models.Model):
    id_libro = models.AutoField(primary_key=True, verbose_name="id del libro")
    nombre_libro = models.CharField(max_length=25, blank=False, null=False,  verbose_name= "nombre del libro")
    autor = models.CharField(max_length=50, blank= False, null=False, verbose_name= "autor del libro")
    fec_salida_libro = models.DateField(blank=False, null=False, verbose_name="fecha de salida del libro")
    precio = models.IntegerField(blank=False, null=False, verbose_name= "precio del libro")
    desc_libro = models.CharField (max_length=200, blank=False, null=False, verbose_name= "descripción del libro")
    portada_libro = models.ImageField(upload_to="portada_libro/")
    
    def __str__(self):
        return self.nombre_libro
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(libro, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.libro.nombre_libro} ({self.quantity})'

