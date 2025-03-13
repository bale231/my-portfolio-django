from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modello per l'appuntamento
class Appointment(models.Model):
    nome_paziente = models.CharField(max_length=255)
    eta = models.IntegerField()
    tipologia_visita = models.CharField(max_length=100, choices=[('Generale', 'Generale'), ('Specialistica', 'Specialistica')])
    diagnosi = models.TextField(blank=True, null=True)
    orario = models.TimeField()
    numero_stanza = models.IntegerField()
    dottore = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    confermato = models.BooleanField(default=False)  # Campo per segnare la conferma
    
    def __str__(self):
        return f"{self.nome_paziente} - {self.orario}"