from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    nombreEmpleado = models.ForeignKey('Empleados',on_delete=models.SET_NULL,null=True) #conecto con la otra tabla o modelo

    def __str__(self):
        return f"Cliente: {self.nombre} -Vendedor: {self.nombreEmpleado.nombre} - [{self.fecha.strftime('%Y-%m-%d %H:%M:%S')}]"
        # Devuelve el nombre del cliente, el nombre del empleado y la fecha en un formato legible


class Empleados(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.nombre