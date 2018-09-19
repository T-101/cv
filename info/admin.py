from django.contrib import admin

from info.models import PersonalInfo, PersonalEmail, PersonalPhoneNumber, ExternalLink, NickName


class PhoneNumberInline(admin.TabularInline):
    model = PersonalPhoneNumber
    can_delete = True


class EmailInline(admin.TabularInline):
    model = PersonalEmail
    can_delete = True


class LinkInline(admin.TabularInline):
    model = ExternalLink
    can_delete = True


class NickNameInline(admin.TabularInline):
    model = NickName
    can_delete = True


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('real_name', 'get_nicks')
    inlines = (PhoneNumberInline, EmailInline, LinkInline, NickNameInline)

    def get_nicks(self, obj):
        return ', '.join([x.name for x in obj.nick_names.all()])
    get_nicks.short_description = 'Nick names'
    get_nicks.admin_order_field = 'nick_names__name'


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
