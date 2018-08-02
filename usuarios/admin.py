# -*- coding: utf-8 -*-

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from usuarios.models import User, Familiar, Avance, CapacitacionInscrita, Community, Training, Trainee, TraineeAdvance

# Register your models here.


class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets + (
        (
            'Información personal 2', {'fields': (
                'id_antiguo', 'tipo_documento', 'documento', 'tipo_usuario', 'is_trainee', 'genero', 'fecha_nacimiento')}
        ), (
            'Ubicación', {'fields': (
                'language', 'pais', 'departamento', 'municipio', 'zona', 'comunidad', 'etnia', 'direccion')}
        ),
        (
            'Contacto', {'fields': (
                'telefono', 'movil')}
        ), (
            'Información PMA', {'fields': (
                'codigo_beneficiario', 'jefe_hogar', 'terminos')}
        ),
    )


class FamiliarAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'familiar', 'parentesco']


class AvanceAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'capacitacion', 'modulo', 'leccion', 'fecha']


class CapacitacionInscritaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'capacitacion']


class TraineeAdmin(admin.ModelAdmin):
    list_display = ['name', 'document', 'date']
    ordering = ('name',)


class TraineeAdvanceAdmin(admin.ModelAdmin):
    list_display = ['trainee', 'capacitation', 'module', 'lesson', 'date']
    search_fields = ('capacitation', 'module',
                     'lesson')
    ordering = ('trainee',)


class CommunityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'state', 'city']

    search_fields = ('country', 'state',
                     'city')
    filter_horizontal = ('trainees',)
    ordering = ('name',)


class TrainingAdmin(admin.ModelAdmin):
    list_display = ['trainer', 'community', 'date']
    search_fields = ('trainer',)
    ordering = ('community',)


admin.site.register(User, UserAdmin)
admin.site.register(Familiar, FamiliarAdmin)
admin.site.register(Avance, AvanceAdmin)
admin.site.register(CapacitacionInscrita, CapacitacionInscritaAdmin)
admin.site.register(Trainee, TraineeAdmin)
admin.site.register(TraineeAdvance, TraineeAdvanceAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(Training, TrainingAdmin)
