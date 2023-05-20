from django.db import models

# Create your models here.

class Viewer(models.Model):
    realname= models.CharField(max_length=25)
    surname= models.CharField(max_length=20)
    mail= models.EmailField()
    img= models.ImageField(blank=False, null=False, upload_to='viewer_images')

    def __str__(self):
        return f"Nombre: {self.realname} |Apellido: {self.surname} |Correo: {self.mail}"

class Streamer(models.Model):
    username= models.CharField(max_length=30)
    mail= models.EmailField()
    desc= models.CharField(max_length=300, blank=True, null=False)
    link= models.CharField(max_length=150)
    img= models.ImageField(blank=False, null=False, upload_to='streamer_images')

    def __str__(self):
        return f"{self.username}"

class Video(models.Model):
    title= models.CharField(max_length=50)
    author= models.ForeignKey(Streamer, on_delete=models.CASCADE)
    mins= models.IntegerField()
    sec= models.IntegerField()
    date= models.DateField()
    link= models.CharField(max_length=300)
    gif= models.CharField(max_length=200)

    def __str__(self):
        return f"Título: {self.title} |Duración: {self.mins}:{self.sec} |Fecha: {self.date} |Autor: {self.author}"


