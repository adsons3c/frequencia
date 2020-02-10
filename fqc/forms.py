from django import forms
from .models import Frequencia_Agentes

class Frequencia_Form(forms.ModelForm):

    class Meta:
        model = Frequencia_Agentes
        fields = ['agente_mobilidade', 'situacao', 'data', 'horario_entrada', 'horario_saida']
