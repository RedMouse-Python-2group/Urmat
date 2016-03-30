from django.contrib import admin

from menu.models import Menu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    fields = ['menu_title', 'menu_description', 'menu_url']

admin.site.register(Menu, MenuAdmin)
