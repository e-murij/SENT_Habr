from django.contrib import admin

from authapp.models import User, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
