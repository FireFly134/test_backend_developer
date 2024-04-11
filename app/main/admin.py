from django.contrib import admin
from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent',)
    list_filter = ('parent',)
    search_fields = ('title', 'parent',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
