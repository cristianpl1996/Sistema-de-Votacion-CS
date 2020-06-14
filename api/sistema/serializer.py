from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class VotanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Votante
        fields = '__all__'
        #fields = ['cedula' ,'nombre', 'apellido' ,'email' ,'telefono' , 'fotografia' ,'contraseña', 'ideleccion']
    def create(self, validated_data):
        validated_data['contraseña'] = make_password(validated_data['contraseña'])
        return super(VotanteSerializer, self).create(validated_data)

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    #votantes = VotanteSerializer(many=True)
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
    