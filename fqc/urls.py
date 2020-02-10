from django.urls import path, include
from .views import  create_frequencia

# app_name = 'frequencia'
urlpatterns = [
    # path('home/', Home.as_view(), name='home'),
    # path('adicionarfrequencia/', Create_Frequencia.as_view(), name='adicionarfrequencia'),
    path ('addfrequencia', create_frequencia, name='addfrequencia')
]
