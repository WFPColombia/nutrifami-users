# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

TIPOS_DOCUMENTO = (
    ('Cédula de ciudadania', 'Cédula de ciudadania'),
    ('Cédula de extranjeria', 'Cédula de extranjeria'),
    ('Tarjeta de identidad', 'Tarjeta de identidad'),
    ('Pasaporte', 'Pasaporte'),
)

PARENTESCO = (
    ('Padre', 'Padre'),
    ('Madre', 'Madre'),
    ('Hermano', 'Hermano'),
    ('Otro', 'Otro'),
)

GENDERS = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Masculino'),
)


class CustomUser(AbstractUser):
        #GENDERS = (('male', 'Male'),('female', 'Female'))
    tipo_documento = models.CharField(
        choices=TIPOS_DOCUMENTO, max_length=45, null=True, verbose_name='Tipos de documento')
    documento = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='documento',  help_text='Número de documento de identidad del usuario',)
    codigo_beneficiario = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='código beneficiario',  help_text='Código asignado por el PMA a sus beneficiarios',)
    jefe_hogar = models.BooleanField(
        default=False, verbose_name='Jefe de hogar', help_text='Determina si el usuario es el jefe de hogar')
    edad = models.PositiveSmallIntegerField(
        blank=True, null=True, verbose_name='edad',  help_text='Edad del usuario',)
    genero = models.CharField(max_length=20, null=True,
                              blank=True, choices=GENDERS)
    fecha_nacimiento = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True,)
    etnia = models.CharField(max_length=45, blank=True, null=True,)
    pais = models.CharField(max_length=45, blank=True, null=True,)
    departamento = models.CharField(max_length=45, blank=True, null=True,)
    municipio = models.CharField(max_length=45, blank=True, null=True,)
    comunidad = models.CharField(max_length=45, blank=True, null=True,)
    zona = models.CharField(max_length=45, blank=True, null=True,)
    direccion = models.CharField(max_length=45, blank=True, null=True,)
    telefono = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='Teléfono')
    movil = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='Telefono móvil')
    social_thumb = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Usuarios"

    def __unicode__(self):
        return unicode(self.username)


class Familiar(models.Model):
    usuario = models.ForeignKey(CustomUser, related_name='usuario')
    familiar = models.ForeignKey(
        CustomUser, related_name='familiar', blank=True)
    parentesco = models.CharField(
        choices=PARENTESCO, max_length=45, blank=True, null=True, verbose_name='Parentesco')

    class Meta:
        verbose_name_plural = "Familiares"

    def __unicode__(self):
        return unicode(self.usuario)
