from django.contrib import admin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group

# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'email', 'phone_number', 'is_admin', 'is_superuser')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields':('email', 'phone_number', 'full_name','username' ,'password')}),
        ('permissions', {'fields':('is_admin', 'is_active', 'is_superuser', 'last_login', 'groups', 'user_permissions')})
    )

    add_fieldsets = (
        (None, {'fields':('phone_number', 'full_name', 'email', 'password1', 'password2')}),
    )

    search_fields = ('email', 'full_name')
    ordering = ('full_name',)
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)

