from django.db import models
from datetime import datetime, date


situacao_choices = (
    ('PRESENTE', 'PRESENTE'),
    ('EXTRA', 'EXTRA'),
    ('FALTA', 'FALTA'),
    ('FALTA JUSTIFICADA', 'FALTA JUSTIFICADA'),
    ('FOLGA', 'FOLGA'),
    ('FERIAS', 'FERIAS'),
    ('LICENÇA', 'LICENÇA'),
    ('PERMUTA', 'PERMUTA'),

    )

class Frequencia_Agentes(models.Model):

    agente_mobilidade = models.CharField(max_length=40)
    situacao = models.CharField(max_length=50, blank=True, null=True, choices=situacao_choices, default='PRESENTE')
    data = models.DateField(auto_now_add=False, auto_now=False)
    horario_entrada = models.TimeField()
    horario_saida = models.TimeField()
    total_hora = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.agente_mobilidade
