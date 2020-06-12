from django.db import models

# Create your models here.

class Resultado(models.Model):
    idresultado = models.AutoField(primary_key=True)
    resultado = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "resultado"
        verbose_name_plural = "resultados"
        
    def __str__(self):
        return self.resultado 

class Eleccion(models.Model):
    ideleccion = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=50, null=True, blank=True)
    hora_inicio = models.CharField(max_length=15, null=True, blank=True)
    hora_final = models.CharField(max_length=15, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    idresultado = models.ForeignKey(Resultado, related_name='elecciones', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "eleccion"
        verbose_name_plural = "elecciones"
        
    def __str__(self):
        return self.nombre 

class Votante(models.Model):
    cedula = models.CharField(max_length=50, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    fotografia = models.ImageField(upload_to="fotografia_votante", null=True, blank=True)
    contraseña = models.CharField(max_length=50)
    ideleccion = models.ForeignKey(Eleccion, related_name='votantes', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "votante"
        verbose_name_plural = "votantes"
        
    def __str__(self):
        return self.nombre

class PartidoPolitico(models.Model):
    idpartido = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=50, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    fotografia = models.ImageField(upload_to="fotografia_partido_politico", null=True)
    
    class Meta:
        verbose_name = "partido_politico"
        verbose_name_plural = "partidos_politicos"
        
    def __str__(self):
        return self.nombre

class Candidato(models.Model):
    cedula = models.CharField(max_length=50, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    fotografia = models.ImageField(upload_to="fotografia_candidato", null=True, blank=True)
    idpartido = models.ForeignKey(PartidoPolitico, related_name='candidatos',null=True, blank=True, on_delete=models.CASCADE)
    ideleccion = models.ForeignKey(Eleccion, related_name='candidatos', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "candidato"
        verbose_name_plural = "candidatos"
        
    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)
    