# -*- coding: utf-8 -*-

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from usuarios.models import CustomUser, Familiar

# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información personal', {'fields': ('genero',)}),
    )


class FamiliarAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'familiar', 'parentesco']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Familiar, FamiliarAdmin)
