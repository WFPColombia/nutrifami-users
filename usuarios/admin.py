from django.contrib import admin

from usuarios.models import CustomUser

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'first_name', 'last_name', 'is_active']
	list_filter = ['groups', 'is_staff', 'is_superuser', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)