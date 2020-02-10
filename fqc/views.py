from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from .forms import *
from datetime import datetime

# class Create_Frequencia(CreateView):
#     u"""Class para adicionar os equipamentos."""
#
#     model = Frequencia_Agentes
#     template_name = 'frequencia/frequencia_form.html'
#     fields = ['agente_mobilidade', 'situacao', 'data', 'horario_entrada', 'horario_saida']
#
#     def form_valid(self, form):
#         u"""Função para validar forms."""
#         try:
#             # total_hora = Frequencia_Agentes
#             form.save()
#             return HttpResponse("OK")
#         except IntegrityError:
#             return HttpResponse("Duplicado")


def create_frequencia(request):
    form = Frequencia_Form()

    if request.method == "POST":
        form = Frequencia_Form(request.POST)

        if form.is_valid():
            # format = '%H:%M:%S'
            frequencia = form.save(commit=False)
            print(type(frequencia.horario_saida))
            frequencia.horario_entrada = datetime.combine(frequencia.data, frequencia.horario_entrada)
            print(frequencia.horario_entrada)
            frequencia.horario_saida = datetime.combine(frequencia.data, frequencia.horario_saida)
            frequencia.total_hora = frequencia.horario_saida - frequencia.horario_entrada
            print(frequencia.total_hora)

            frequencia.save()

            return HttpResponseRedirect('/sce/listequipamentos')

    return render(request, "frequencia/frequencia_form.html", locals())
