from django.contrib import admin

from accounts.models import Profile, Comment

# Register your models here.

admin.site.register(Profile)
admin.site.register(Comment)