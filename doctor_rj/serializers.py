# -*- coding: utf-8 -*-
from rest_framework import serializers

from doctor_rj.models import Establishment


class EstabelecimentoSerializer(serializers.Serializer):

    nome = serializers.CharField(max_length=60, source='common_name')
    telefone = serializers.CharField(max_length=60, source='phone')
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    esfera_administrativa = serializers.SerializerMethodField()
    logradouro = serializers.SerializerMethodField()

    def get_logradouro(self, obj):
        return "%s, %s/%s - %s" % (obj.address, obj.number, obj.add_address, obj.district)

    def get_esfera_administrativa(self, obj):
        return True if str(obj.administrative.name) == str("PRIVADA") else False


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
