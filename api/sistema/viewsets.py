from rest_framework import viewsets
from .models import *
from .serializer import *

class VotanteViewSet(viewsets.ModelViewSet):
    queryset =  Votante.objects.all()
    serializer_class = VotanteSerializer

class EleccionViewSet(viewsets.ModelViewSet):
    queryset =  Eleccion.objects.all()
    serializer_class = EleccionSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset =  Resultado.objects.all()
    serializer_class = ResultadoSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset =  Candidato.objects.all()
    serializer_class = CandidatoSerializer

class PartidoPoliticoViewSet(viewsets.ModelViewSet):
    queryset =  PartidoPolitico.objects.all()
    serializer_class = PartidoPoliticoSerializer