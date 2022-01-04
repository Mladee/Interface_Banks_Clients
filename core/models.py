from django.db import models


class Banci(models.Model):

    
    nume = models.CharField(max_length=45,null=True)
    adresa = models.CharField(max_length=45,null = True)
   
    def __str__(self):
        return f'{self.nume}  {self.adresa}'
        

class Clienti(models.Model):
    
    
    nume = models.CharField(max_length = 45,null=True)
    prenume = models.CharField(max_length = 45,null=True)
    adresa = models.CharField(max_length=45,null=True)
    data_nasterii = models.DateTimeField(null=True)
    salariu = models.FloatField(null=True)
    functie = models.CharField(max_length = 45,null=True)

    def __str__(self):
        return f'{self.nume} {self.prenume}'
    

class Asociere_Imprumuturi(models.Model):

   
    banci = models.ForeignKey(Banci, on_delete=models.CASCADE,null=True)
    clienti = models.ForeignKey(Clienti, on_delete=models.CASCADE,null=True)
    data_imprumut = models.DateTimeField(null=True)
    termen_scadent = models.DateTimeField(null=True)
    dobanda = models.FloatField(null=True)
    suma = models.FloatField(null=True)

    def __str__(self):
        return f'{self.banci.nume} {self.clienti.nume} {self.clienti.prenume} {self.id}'





