# -*- coding: utf-8 -*-
import json
import requests
from django.core.management.base import BaseCommand
from doctor_rj.models import Administrative, TeachingActivity, OrganizationNature, UnitType, Establishment

class Command(BaseCommand):
    help = "Command to get establishments json."

    def handle(self, *args, **options):

    	url = "http://dadosabertos.rio.rj.gov.br/apiSaude/apresentacao/rest/index.cfm/estabelecimentos"

    	try:
    		req = requests.get(url)
    		if req.ok:
    			content = unicode(req.content, errors='ignore')
    			data = json.loads(content)

    			for establishment in data.get("DATA"):
					try:
						cnes = long(establishment[0]) if establishment[0] != '' else establishment[0]
						cnpj = long(establishment[1]) if establishment[1] != '' else establishment[1]
						razao_social = establishment[2]
						nome_de_fantasia = establishment[3]
						logradouro = establishment[4]
						numero = int(establishment[5]) if not isinstance(establishment[5], unicode) else establishment[5]
						complemento = establishment[6]
						bairro = establishment[7]
						cep = int(establishment[8])
						telefone = long(establishment[9]) if not isinstance(establishment[9], unicode) else establishment[9]
						fax = establishment[10]
						email = establishment[11]
						latitude = establishment[12]
						longitude = establishment[13]
						data_atualizacao = establishment[14]

						codigo_esfera_adm = int(establishment[15])
						esfera_adm = establishment[16]
						administrative = self._get_administrative(codigo_esfera_adm, esfera_adm)

						codigo_atividade = int(establishment[17])
						atividade_de_destino = establishment[18]
						teaching_activity = self._get_teaching_activity(codigo_atividade, atividade_de_destino)

						codigo_natureza_organizacao = int(establishment[19])
						natureza_organizacao = establishment[20]
						organization_nature = self._get_organization_nature(codigo_natureza_organizacao, natureza_organizacao)

						tipo_da_unidade = int(establishment[21])
						tipo_de_estabelecimento = establishment[22]
						unit_type = self._get_unit_type(tipo_da_unidade, tipo_de_estabelecimento)

						estabelecimento = Establishment(
							cnes=cnes, cnpj=cnpj, company_name=razao_social, common_name=nome_de_fantasia, address=logradouro, number=numero,
							add_address=complemento, district=bairro, cep=cep, phone=telefone, fax=fax, email=email, latitude=latitude,
							longitude=longitude, coordinates_update=data_atualizacao,
						)
						estabelecimento.administrative = administrative
						estabelecimento.teaching_activity = teaching_activity
						estabelecimento.organization_nature = organization_nature
						estabelecimento.unit_type = unit_type
						estabelecimento.save()

					except Exception, e:
						pass
						import ipdb; ipdb.set_trace()

    	except Exception, e:
    		print e     

    def _get_administrative(self, codigo_esfera_adm, esfera_adm):

    	try:
    		administrative = Administrative.objects.get(code=codigo_esfera_adm)
    	except Administrative.DoesNotExist:
    		administrative = Administrative(code=codigo_esfera_adm, name=esfera_adm)
    		administrative.save()

    	return administrative

    def _get_teaching_activity(self, codigo_atividade, atividade_de_destino):

    	try:
    		teaching_activity = TeachingActivity.objects.get(code=codigo_atividade)
    	except TeachingActivity.DoesNotExist:
    		teaching_activity = TeachingActivity(code=codigo_atividade, activity_type= atividade_de_destino)
    		teaching_activity.save()

    	return teaching_activity

    def _get_organization_nature(self, codigo_natureza_organizacao, natureza_organizacao):

    	try:
    		organization_nature = OrganizationNature.objects.get(code=codigo_natureza_organizacao)
    	except OrganizationNature.DoesNotExist:
    		organization_nature = OrganizationNature(code=codigo_natureza_organizacao, nature=natureza_organizacao)
    		organization_nature.save()

    	return organization_nature

    def _get_unit_type(self, tipo_da_unidade, tipo_de_estabelecimento):

    	try:
    		unit_type = UnitType.objects.get(code=tipo_da_unidade)
    	except UnitType.DoesNotExist:
    		unit_type = UnitType(code=tipo_da_unidade, name=tipo_de_estabelecimento)
    		unit_type.save()

    	return unit_type