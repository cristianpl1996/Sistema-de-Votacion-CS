from rest_framework import serializers
from .models import *

class VotanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Votante
        fields = '__all__'
        #fields = ['cedula' ,'nombre', 'apellido' ,'email' ,'telefono' , 'fotografia' ,'contraseña', 'ideleccion']

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    #idpartido = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')
    class Meta:
        model = Candidato
        fields = '__all__'
        #fields = ['cedula', 'nombre', 'apellido', 'telefono', 'fotografia', 'idpartido', 'ideleccion']

class EleccionSerializer(serializers.HyperlinkedModelSerializer):
    votantes = VotanteSerializer(many=True)
    candidatos = CandidatoSerializer(many=True)
    class Meta:
        model = Eleccion
        fields = '__all__'
        #fields = ['ideleccion', 'fecha', 'hora_inicio', 'hora_final', 'descripcion', 'idresultado', 'votantes', 'candidatos']

class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    elecciones = EleccionSerializer(many=True)
    class Meta:
        model = Resultado
        fields = '__all__'
        #fields = ['idresultado', 'resultado', 'elecciones']

class PartidoPoliticoSerializer(serializers.ModelSerializer):
    candidatos = CandidatoSerializer(many=True)
    class Meta:
        model = PartidoPolitico
        fields = '__all__'
        #fields = ['idpartido', 'nit', 'nombre', 'direccion', 'fotografia', 'candidatos']
    