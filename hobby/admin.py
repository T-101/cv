from django.contrib import admin

from hobby.models import Hobby, HobbyItem


class HobbyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'sort_order')
    search_fields = ('name', 'description', 'hobbyitems__text')
    list_editable = ('sort_order',)


admin.site.register(Hobby, HobbyAdmin)


class HobbyItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'hobby', 'sort_order')
    search_fields = ('text',)
    list_editable = ('sort_order',)
    list_filter = ('hobby',)


admin.site.register(HobbyItem, HobbyItemAdmin)
