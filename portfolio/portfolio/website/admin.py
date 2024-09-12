from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'age', 'location', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'age', 'location', 'bio')}),
    )
    list_display = ('username', 'email', 'name', 'age', 'location', 'bio', 'is_staff')
    search_fields = ('username', 'email', 'name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

