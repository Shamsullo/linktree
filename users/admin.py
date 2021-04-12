from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fields_list = ('phone_number', 'first_name', 'last_name', 'birthdate', 'is_staff', 'is_active',)
    list_display = fields_list
    list_filter = fields_list
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal data', {'fields': ('first_name', 'last_name', 'birthdate')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'is_staff',
                       'first_name', 'last_name', 'birthdate')
        }),
    )
    search_fields = ('phone_number', 'first_name', 'last_name')
    ordering = ('date_joined',)


admin.site.register(CustomUser, CustomUserAdmin)
