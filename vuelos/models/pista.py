import uuid

from django.db import models
from pathlib import Path
from django.db import models

def pista_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'tablas/{uuid.uuid4()}{ext}'

class Pista(models.Model):
    id_pista = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    estado = models.CharField(max_length=20)
    image       = models.ImageField(upload_to=pista_image_path, blank=True, null=True)

    class Meta:
        db_table = 'pista'