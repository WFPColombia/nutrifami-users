# -*- coding: utf-8 -*-

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from usuarios.models import User, Familiar

# Register your models here.


class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información personal', {'fields': ('genero',)}),
    )


class FamiliarAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'familiar', 'parentesco']


admin.site.register(User, UserAdmin)
admin.site.register(Familiar, FamiliarAdmin)
