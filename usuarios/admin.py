# -*- coding: utf-8 -*-

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from usuarios.models import User, Familiar, Avance, CapacitacionInscrita

# Register your models here.


class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            'Información personal 2', {'fields': (
                'tipo_documento', 'documento', 'genero', 'fecha_nacimiento')}
        ), (
            'Ubicación', {'fields': (
                'pais', 'departamento', 'municipio', 'zona', 'comunidad', 'etnia', 'direccion')}
        ),
        (
            'Contacto', {'fields': (
                'telefono', 'movil')}
        ), (
            'Información PMA', {'fields': (
                'codigo_beneficiario', 'jefe_hogar')}
        ),
    )


class FamiliarAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'familiar', 'parentesco']


class AvanceAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'capacitacion', 'modulo', 'leccion']


class CapacitacionInscritaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'capacitacion']

admin.site.register(User, UserAdmin)
admin.site.register(Familiar, FamiliarAdmin)
admin.site.register(Avance, AvanceAdmin)
admin.site.register(CapacitacionInscrita, CapacitacionInscritaAdmin)
