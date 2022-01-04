from django.forms import ModelForm
from core.models import Banci,Clienti,Asociere_Imprumuturi


class BanciForm(ModelForm):
    class Meta:
        model = Banci
        fields = '__all__'

class ClientiForm(ModelForm):
    class Meta:
        model = Clienti
        fields = '__all__'


class ImprumuturiForm(ModelForm):
    class Meta:
        model = Asociere_Imprumuturi
        fields = '__all__'