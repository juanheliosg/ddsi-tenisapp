from django.shortcuts import render
from .models import Tenista, Compra, Tenistaedicionentrenador, Asignado, Partido
from .serializers import TenistaSerializer, AsignadoSerializer, PartidoSerializer, CompraSerializer
from rest_framework import generics, viewsets

# Create your views here.

class TenistaNoInscritosView(generics.ListAPIView):
    serializer_class = TenistaSerializer
    #En este método definimos 
    def get_queryset(self):
        #Version raw sql no recomendada por django
        edicion = self.kwargs['edicion'] #Cogemos los argumentos de la url en este caso de la edición
        return Tenista.objects.raw( "SELECT * FROM TENISTA WHERE NOT EXISTS ( SELECT * FROM TENISTAEDICIONENTRENADOR WHERE IDEdicion = {} AND Tenista.IDTenista = TenistaEdicionEntrenador.IDTenista);".format(edicion))

        
        #Para hacerla consulta tenemos que dividirla en dos partes. Primero cogemos los ids de los tenistas que no
        #En esa edición y después lo unimos con la tabla de tenistas
        #ids = Tenistaedicionentrenador.objects.exclude(idedicion__exact = edicion).values('idtenista')[0]
        #return Tenista.objects.filter(idtenista = ids)

class AsignadoSet(viewsets.ModelViewSet):
	queryset = Asignado.objects.all()
	serializer_class = AsignadoSerializer

class PartidoSet(viewsets.ModelViewSet):
	queryset = Partido.objects.all()
	serializer_class = PartidoSerializer

class CompraSet(viewsets.ModelViewSet):
        queryset = Compra.objects.all()
        serializer_class = CompraSerializer
