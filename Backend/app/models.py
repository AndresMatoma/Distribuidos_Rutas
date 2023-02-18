from django.db import models

# Create your models here.
#modelo Buse
class Bus (models.Model):
    id_bus = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    marca = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    def __str__(self):
        return str(self.matricula)

#modelo paradero
class Paradero(models.Model):
    id_paradero = models.AutoField(primary_key=True)
    latitud = models.DecimalField(max_digits=15, decimal_places=4)
    longitud = models.DecimalField(max_digits=15, decimal_places=4)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre)    

#modelo horario
class Horario(models.Model):
    id_hora = models.AutoField(primary_key=True)
    horario = models.TimeField()
    def __str__(self):
        return str(self.horario)

#modelo Rutas
class Ruta (models.Model):
    id_ruta = models.AutoField(primary_key=50)
    paradero=models.ForeignKey(Paradero,on_delete=models.CASCADE,related_name='genera')
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE,related_name='tiene')
    hora = models.ForeignKey(Horario,on_delete=models.CASCADE,related_name='tiene')
    def __str__(self):
        return str(self.id_ruta)
