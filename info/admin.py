from django.contrib import admin

from info.models import PersonalInfo, Email, PhoneNumber, ExternalLink, NickName, Detail, DetailItem, Picture


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    can_delete = True


class EmailInline(admin.TabularInline):
    model = Email
    can_delete = True


class LinkInline(admin.TabularInline):
    model = ExternalLink
    can_delete = True


class NickNameInline(admin.TabularInline):
    model = NickName
    can_delete = True


class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('real_name', 'title', 'get_nicks')
    inlines = (PhoneNumberInline, EmailInline, LinkInline, NickNameInline)

    def get_nicks(self, obj):
        return ', '.join([x.name for x in obj.nick_names.all()])

    get_nicks.short_description = 'Nick names'
    get_nicks.admin_order_field = 'nick_names__name'


admin.site.register(PersonalInfo, PersonalInfoAdmin)


class PersonalEmailAdmin(admin.ModelAdmin):
    list_display = ('address',)


admin.site.register(Email, PersonalEmailAdmin)


class PersonalPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'number',)


admin.site.register(PhoneNumber, PersonalPhoneNumberAdmin)


class ExternalLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(ExternalLink, ExternalLinkAdmin)


class NickNameAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')


admin.site.register(NickName, NickNameAdmin)


class DetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_order')
    list_editable = ('sort_order',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Detail, DetailAdmin)


class DetailItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'detail', 'text', 'sort_order')
    search_fields = ('text',)
    list_editable = ('sort_order',)
    list_filter = ('detail__name',)


admin.site.register(DetailItem, DetailItemAdmin)


class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image')


admin.site.register(Picture, PictureAdmin)
