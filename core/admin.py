from django.contrib import admin
from . import models
# Register your models here.


class BanciAdmin(admin.ModelAdmin):
    list_display = ['id','nume','adresa']
    list_editable = ['adresa']
    list_per_page = 10

class ClientiAdmin(admin.ModelAdmin):
    list_display = ['id','nume','prenume','adresa','data_nasterii','salariu','functie']
    list_editable = ['adresa','salariu','functie']
    list_per_page = 10

class AsociereImprumuturiAdmin(admin.ModelAdmin):
    list_display = ['id','data_imprumut','termen_scadent','dobanda','suma','banci_id','clienti_id','banci','clienti']
    list_per_page = 10




admin.site.register(models.Banci, BanciAdmin)
admin.site.register(models.Clienti,ClientiAdmin)
admin.site.register(models.Asociere_Imprumuturi,AsociereImprumuturiAdmin)