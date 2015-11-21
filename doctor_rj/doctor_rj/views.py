# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from doctor_rj.models import Establishment
from doctor_rj.serializers import EstabelecimentoSerializer
from django.http import HttpResponse

class EstabelecimentoView(viewsets.ModelViewSet):

	queryset = Establishment.objects.all()
	serializer_class = EstabelecimentoSerializer

class EstabelecimentoList(generics.ListAPIView):

	serializer_class = EstabelecimentoSerializer

	def get_queryset(self):
		return Establishment.objects.all()

class EstabelecimentoDetail(generics.ListAPIView):

	serializer_class = EstabelecimentoSerializer

	def get_queryset(self):

		id = self.kwargs.get('pk')
		return Establishment.objects.filter(id=id)