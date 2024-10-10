from django.db import models

# Create your models here.
class TipoPeriodista(models.Model):
    descripcion = models.CharField(max_length=40)
    def __str__(self):
        return self.descripcion

class Periodista(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=14)
    fecha_contrato= models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=10, choices=[('masculino','Masculino'),('femenino','Femenino')])
    TipoPeriodista = models.ForeignKey(TipoPeriodista, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="periodistas",blank=True,null=True)

    def __str__(self):
        return self.nombre
    
class TipoNoticia(models.Model):
    descripcion = models.CharField(max_length=40)
    def __str__(self):
        return self.descripcion
    
class Noticia(models.Model):
    periodista = models.ForeignKey(Periodista, on_delete=models.CASCADE)
    TipoNoticia = models.ForeignKey(TipoNoticia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="noticias", null=True)
    estado = models.CharField(max_length=10, choices=[('aprobado','Aprobado'),('rechazado','Rechazado'),('pendiente','Pendiente')], default='pendiente')
    motivo = models.CharField(max_length=5000,blank=True,null=True)


    def __str__(self):
        return self.titulo
