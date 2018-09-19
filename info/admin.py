from django.contrib import admin

from info.models import PersonalInfo, PersonalEmail, PersonalPhoneNumber, ExternalLink, NickName


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('real_name',)


admin.site.register(PersonalInfo, PersonalInfoAdmin)


class PersonalEmailAdmin(admin.ModelAdmin):
    list_display = ('address',)


admin.site.register(PersonalEmail, PersonalEmailAdmin)


class PersonalPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'number',)


admin.site.register(PersonalPhoneNumber, PersonalPhoneNumberAdmin)


class ExternalLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(ExternalLink, ExternalLinkAdmin)


class NickNameAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')


admin.site.register(NickName, NickNameAdmin)
