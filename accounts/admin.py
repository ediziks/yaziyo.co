from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'pk', 'email')
  search_fields = ('user__username', 'pk', 'email')


admin.site.register(Profile, ProfileAdmin)
