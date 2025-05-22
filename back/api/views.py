from django.shortcuts import render
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated



class OrdemServicoView(ListCreateAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    permission_classes = [IsAuthenticated]

class PatrimoniosView(ListCreateAPIView):
    queryset = Patrimonios.objects.all()
    serializer_class = PatrimonioSerializer
    permission_classes = [IsAuthenticated]

class AmbientesView(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbienteSerializer
    permission_classes = [IsAuthenticated]

class FuncionariosView(ListCreateAPIView):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]


class AreaView(ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]
