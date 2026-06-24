from django.db import models

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)

    class Meta:
        db_table = 'empleado'

    def __str__(self):
        return self.nombre