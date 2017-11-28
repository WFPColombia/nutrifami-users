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


class User(AbstractUser):
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
    movil2 = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='Telefono móvil 2')
    social_thumb = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Usuarios"

    def __unicode__(self):
        return unicode(self.username)


class Familiar(models.Model):
    usuario = models.ForeignKey(User, related_name='familiar_usuario')
    familiar = models.ForeignKey(
        User, related_name='familiar_familiar', blank=True)
    parentesco = models.CharField(
        choices=PARENTESCO, max_length=45, blank=True, null=True, verbose_name='Parentesco')

    class Meta:
        verbose_name_plural = "Familiares"

    def __unicode__(self):
        return unicode(self.usuario)


class Avance(models.Model):
    usuario = models.ForeignKey(User, related_name='avance_usuario')
    capacitacion = models.PositiveIntegerField(
        verbose_name='Id Capacitación',  help_text='Número de id de la capacitación',)
    modulo = models.PositiveIntegerField(
        verbose_name='Id  Módulo',  help_text='Número de id del módulo',)
    leccion = models.PositiveIntegerField(
        verbose_name='Id Lección',  help_text='Número de id de la lección',)

    class Meta:
        verbose_name_plural = "Avance"


class CapacitacionInscrita(models.Model):
    usuario = models.ForeignKey(
        User, related_name='capacitacioninscrita_usuario')
    capacitacion = models.PositiveIntegerField(
        verbose_name='Id Capacitación',  help_text='Número de id de la capacitación',)

    class Meta:
        verbose_name_plural = "Capacitaciones Inscritas"

    def __unicode__(self):
        return unicode(self.usuario)
