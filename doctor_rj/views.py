# -*- coding: utf-8 -*-

from rest_framework import viewsets, generics

from doctor_rj.models import Establishment
from doctor_rj.models import UnitType
from doctor_rj.serializers import EstabelecimentoSerializer
from doctor_rj.serializers import TipoUnidadeSerializer


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


class EstabelecimentoPorTipoList(generics.ListAPIView):

	serializer_class = TipoUnidadeSerializer

	def get_queryset(self):

		return UnitType.objects.all()

