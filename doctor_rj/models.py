# -*- coding: utf-8 -*-
from django.db import models


class Establishment(models.Model):
    cnes = models.CharField(max_length=7, blank=False, null=False)
    cnpj = models.CharField(max_length=14, blank=False, null=False)
    company_name = models.CharField(max_length=60, blank=False, null=False)
    common_name = models.CharField(max_length=60, blank=False, null=False)
    address = models.CharField(max_length=60, blank=False, null=False)
    number = models.CharField(max_length=10, blank=False, null=False)
    add_address = models.CharField(max_length=60, blank=False, null=False)
    district = models.CharField(max_length=60, blank=False, null=False)
    cep = models.CharField(max_length=60, blank=False, null=False)
    phone = models.CharField(max_length=60, blank=False, null=False)
    fax = models.CharField(max_length=60, blank=False, null=False)
    email = models.CharField(max_length=60, blank=False, null=False)
    latitude = models.CharField(max_length=60, blank=False, null=False)
    longitude = models.CharField(max_length=60, blank=False, null=False)
    coordinates_update = models.CharField(max_length=60, blank=True, null=True)
    administrative = models.ForeignKey('Administrative', blank=False, null=False)
    teaching_activity = models.ForeignKey('TeachingActivity', null=False)
    organization_nature = models.ForeignKey('OrganizationNature', null=False)
    unit_type = models.ForeignKey('UnitType', null=False)

    class Meta(object):
        verbose_name = u'Estabelecimento'
        verbose_name_plural = u'Estabelecimentos'

    def __unicode__(self):
        return u"%s" % self.common_name


class Administrative(models.Model):
    code = models.CharField(max_length=2, blank=False, null=False, verbose_name=u'Código da Esfera Administrativa')
    name = models.CharField(max_length=60, blank=False, null=False, verbose_name=u'Esfera Administrativa')

    class Meta(object):
        verbose_name = u'Esfera Administrativa'
        verbose_name_plural = u'Esferas Administrativas'

    def __unicode__(self):
        return u"%s-%s" % (self.code, self.name)


class TeachingActivity(models.Model):
    code = models.CharField(max_length=2, blank=False, null=False, verbose_name=u'Código da Atividade de Ensino')
    activity_type = models.CharField(max_length=60, blank=False, null=False, verbose_name=u'Atividade de Ensino')

    class Meta(object):
        verbose_name = u'Atividade de Ensino'
        verbose_name_plural = u'Atividades de Ensino'

    def __unicode__(self):
        return u"%s-%s" % (self.code, self.activity_type)


class OrganizationNature(models.Model):
    code = models.CharField(max_length=2, blank=False, null=False, verbose_name=u'Código da Natureza da Organização')
    nature = models.CharField(max_length=60, blank=False, null=False, verbose_name=u'Natureza da Organização')

    class Meta(object):
        verbose_name = verbose_name_plural = u'Natureza da Organização'

    def __unicode__(self):
        return u"%s-%s" % (self.code, self.nature)


class UnitType(models.Model):
    code = models.CharField(max_length=2, blank=False, null=False, verbose_name=u'Código do Tipo da Unidade')
    name = models.CharField(max_length=60, blank=False, null=False, verbose_name='Tipo de Estabelecimento')

    class Meta(object):
        verbose_name = verbose_name_plural = u'Tipo da Unidade'

    def __unicode__(self):
        return u"%s-%s" % (self.code, self.name)
