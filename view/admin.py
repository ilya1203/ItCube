from django.contrib import admin

from .models import People

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('Name', 'YearsOne', 'YearsTwo', 'Place')
    list_display_links = ('Name', 'YearsOne', 'YearsTwo', 'Place')
    search_fields = ('Name', 'YearsOne', 'YearsTwo', 'Place')
admin.site.register(People, PeopleAdmin)
# Register your models here.
