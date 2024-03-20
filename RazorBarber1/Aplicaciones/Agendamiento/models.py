from django.db import models

# Create your models here.

from django.db import models

class Rol(models.Model):
    tipoRol = models.CharField(max_length=45)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.tipoRol, self.id)
    
class Administrador(models.Model):
    idAdministrador = models.CharField(max_length=15, primary_key=True)
    correoE = models.CharField(max_length=45)
    clave = models.CharField(max_length=30)
    idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.correoE,self.idAdministrador)

class Barbero(models.Model):
    idBarbero = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correoE = models.CharField(max_length=45)
    clave = models.CharField(max_length=30)
    idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.correoE, self.idBarbero)

class Cliente(models.Model):
    idCliente = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correoE = models.CharField(max_length=45)
    celular = models.CharField(max_length=45)
    clave = models.CharField(max_length=30)
    idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.correoE, self.idCliente)

class Servicio(models.Model):
    tipoServicio = models.CharField(max_length=45)
    precio = models.IntegerField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.tipoServicio, self.id)

class Agenda(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idBarbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    codigoUnico = models.CharField(max_length=45)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.idCliente)

class Asistencia(models.Model):
    idAgenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    estado = models.CharField(max_length=45)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.estado, self.idAgenda)

class Calificacion(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idBarbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    descripcion = models.TextField()
    calificacion = models.IntegerField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.calificacion)

class Horario(models.Model):
    idBarbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    horaInicio = models.TimeField()
    horaFinal = models.TimeField()
    diaDescanso = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.idBarbero, self.horaInicio, self.horaFinal, self.diaDescanso}'
        
class RegistroPago(models.Model):
    idAgenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    servicioAdicional = models.CharField(max_length=45)
    montoPagado = models.IntegerField()
    
    def __str__(self):
        return f'{self.id,self.idAgenda,self.servicioAdicional,self.montoPagado}'
