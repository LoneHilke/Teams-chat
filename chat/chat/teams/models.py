from django.db import models

# Create your models here.
class Links (models.Model):
    Title = models.CharField(max_length=100)
    Fra_JQ = models.URLField(blank=True)
    Beskrivelse = models.TextField(blank=True)
    Sendt = models.DateField()
    Fra_F_LH = models.URLField(blank=True)
    Beskriv = models.TextField(blank=True)
    #Fuldført = models.CheckConstraint(blank=True)
