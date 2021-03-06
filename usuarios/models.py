# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

TIPOS_DOCUMENTO = (
    ('Cédula de ciudadania', 'Cédula de ciudadania'),
    ('Otro', 'Otro'),
    ('Pasaporte', 'Pasaporte'),
)

TIPOS_USUARIOS = (
    ('Director', 'Director'),
    ('Profesor', 'Profesor'),
    ('Encargado del Comedor', 'Encargado del Comedor'),
    ('Cocinero', 'Cocinero'),
    ('Jefe de Cocina', 'Jefe de Cocina'),
    ('Comité de Gestión', 'Comité de Gestión'),
    ('Estudiante', 'Estudiante'),
    ('Otro', 'Otro'),
)

PARENTESCO = (
    ('Padre', 'Padre'),
    ('Madre', 'Madre'),
    ('Hermano', 'Hermano'),
    ('Otro', 'Otro'),
)

GENDERS = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
)

ETNIAS = (
    ('Afrocolombianos', 'Afrocolombianos'),
    ('Indigenas', 'Indigenas'),
    ('Mestizo', 'Mestizo'),
    ('Otros', 'Otros'),
    ('Ninguno', 'Ninguno'),
)

LANGUAGES = (
    ('es', 'es'),
    ('en', 'en'),
    ('fr', 'fr'),
)

class User(AbstractUser):
    id_antiguo = models.PositiveIntegerField(
        blank=True, null=True, unique=True, verbose_name='id antiguo',  help_text='Id de la antigua base de datos',)
    email = models.EmailField(
        verbose_name='Correo electrónico',
        max_length=255,
        null=True,
        blank=True
    )
    tipo_documento = models.CharField(
        choices=TIPOS_DOCUMENTO, max_length=45, blank=True, null=True, verbose_name='Tipo de documento')
    documento = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='documento',  help_text='Número de documento de identidad del usuario',)
    codigo_beneficiario = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='código beneficiario',  help_text='Código asignado por el PMA a sus beneficiarios',)
    jefe_hogar = models.BooleanField(
        default=False, verbose_name='Jefe de hogar', help_text='Determina si el usuario es el jefe de hogar')
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
    terminos = models.BooleanField(
        default=False, verbose_name='Términos y condiciones', help_text='El usuario aceptó términos y cóndiciones')

    tipo_usuario = models.CharField(
        choices=TIPOS_USUARIOS, max_length=45, blank=True, null=True, verbose_name='Tipo de usuario')

    language = models.CharField(
        choices=LANGUAGES, max_length=45, blank=True, null=True, verbose_name='Idioma del usuario')
    is_trainee = models.BooleanField(
        default=False, verbose_name='Is trainee', help_text='For a person who did made the capacitation offline')

    class Meta:
        verbose_name_plural = "Usuarios"

    def __unicode__(self):
        return unicode(self.username)


class Familiar(models.Model):
    usuario = models.ForeignKey(User, related_name='familiar_usuario', on_delete=models.CASCADE)
    familiar = models.ForeignKey(
        User, related_name='familiar_familiar', blank=True, on_delete=models.CASCADE)
    parentesco = models.CharField(
        choices=PARENTESCO, max_length=45, blank=True, null=True, verbose_name='Parentesco')

    class Meta:
        verbose_name_plural = "Familiares"

    def __unicode__(self):
        return unicode(self.usuario)


class Avance(models.Model):
    usuario = models.ForeignKey(
        User, related_name='avances', on_delete=models.CASCADE)
    capacitacion = models.PositiveIntegerField(
        verbose_name='Id Capacitación',  help_text='Número de id de la capacitación',)
    modulo = models.PositiveIntegerField(
        verbose_name='Id  Módulo',  help_text='Número de id del módulo',)
    leccion = models.PositiveIntegerField(
        verbose_name='Id Lección',  help_text='Número de id de la lección',)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Avance"


class CapacitacionInscrita(models.Model):
    usuario = models.ForeignKey(
        User, related_name='capacitacioninscrita_usuario', on_delete=models.CASCADE)
    capacitacion = models.PositiveIntegerField(
        verbose_name='Id Capacitación',  help_text='Número de id de la capacitación',)

    class Meta:
        verbose_name_plural = "Capacitaciones Inscritas"

    def __unicode__(self):
        return unicode(self.usuario)


class Trainee(models.Model):
    name = models.CharField(max_length=45,)
    document = models.PositiveIntegerField(
        help_text='Número de documento de identidad del aprendiz',)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Trainees"

    def __unicode__(self):
        return unicode(self.name)


class TraineeAdvance (models.Model):
    trainee = models.ForeignKey(
        Trainee, related_name='trainieeadvence_trainee', on_delete=models.CASCADE)
    capacitation = models.PositiveIntegerField(
        verbose_name='Id Capacitación',  help_text='Número de id de la capacitación',)
    module = models.PositiveIntegerField(
        verbose_name='Id  Módulo',  help_text='Número de id del módulo',)
    lesson = models.PositiveIntegerField(
        verbose_name='Id Lección',  help_text='Número de id de la lección',)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Trainees Advances"

    def __unicode__(self):
        return unicode(self.trainee.name)


class Community(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True,)
    country = models.CharField(max_length=45, blank=True, null=True,)
    state = models.CharField(max_length=45, blank=True, null=True,)
    city = models.CharField(max_length=45, blank=True, null=True,)
    trainees = models.ManyToManyField(Trainee, blank=True)

    class Meta:
        verbose_name_plural = "Communities"

    def __unicode__(self):
        return unicode(self.name)


class Training(models.Model):
    trainer = models.ForeignKey(User, related_name='training_trainer', on_delete=models.CASCADE)
    community = models.ForeignKey(Community, related_name='training_community', on_delete=models.CASCADE)
    date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True,)

    class Meta:
        verbose_name_plural = "Trainings"

    def __unicode__(self):
        return unicode(self.community)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
