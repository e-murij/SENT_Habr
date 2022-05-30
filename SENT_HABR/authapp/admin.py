from django import forms
from django.contrib import admin

from authapp.models import User, UserProfile


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_verify', 'is_staff', 'is_superuser')


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_verify', 'is_staff', 'is_superuser')
    list_display_links = (
        'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_verify', 'is_staff', 'is_superuser')
    form = UserAdminForm


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'birthday', 'gender')
    list_display_links = ('id', 'user', 'birthday', 'gender')


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
