# -*- coding: utf-8 -*-
import json
from rest_framework import serializers
from doctor_rj.models import Establishment


class EstabelecimentoSerializer(serializers.Serializer):

	nome = serializers.CharField(max_length=60, source='common_name')
	razao_social = serializers.CharField(max_length=60, source='company_name')
	cnes = serializers.CharField(max_length=7)
	cnpj = serializers.CharField(max_length=14)
	endereco = serializers.CharField(max_length=60, source='address')
	numero = serializers.CharField(max_length=10, source='number')
	complemento = serializers.CharField(max_length=60, source='add_address')
	bairro = serializers.CharField(max_length=60, source='district')
	cep = serializers.CharField(max_length=60)
	telefone = serializers.CharField(max_length=60, source='phone')
	email = serializers.CharField(max_length=60)
	latitude = serializers.CharField(max_length=60)
	longitude = serializers.CharField(max_length=60)
	natureza_organizacao = serializers.SlugRelatedField(source='organization_nature', read_only=True, slug_field='nature')
	esfera_administrativa = serializers.SlugRelatedField(source='administrative', read_only=True, slug_field='name')
	atividade_de_ensino = serializers.SlugRelatedField(
		source='teaching_activity', read_only=True, slug_field='activity_type'
	)
	tipo_da_unidade = serializers.SlugRelatedField(source='unit_type', read_only=True, slug_field='name')


class TipoUnidadeSerializer(serializers.Serializer):

	nome = serializers.CharField(max_length=60, source='name')
	estabelecimentos = serializers.SerializerMethodField('get_estabelecimentos_list')

	def get_estabelecimentos_list(self, obj):

		estabelecimentos = Establishment.objects.filter(unit_type=obj)
		data = list()
		for estabelecimento in estabelecimentos:
			est = EstabelecimentoSerializer(estabelecimento)
			data.append(est.data)
		return data
