from django.contrib import admin

from .models import Email, PhoneNumber, Picture, PersonalInfo, DetailCategory, DetailItem, Employer, Employment, \
    EmploymentTask, Hobby, HobbyItem, ExternalLink


# InLines

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'primary', 'address', 'user')
    list_filter = ('primary', 'user')


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'fa_class', 'user')
    list_filter = ('user',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'picture')
    list_filter = ('user',)


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    inlines = [EmailInline, PhoneNumberInline]


@admin.register(DetailCategory)
class DetailCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sort_order']
    list_editable = ['sort_order']


@admin.register(DetailItem)
class DetailItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'detail_category', 'text', 'sort_order']
    list_editable = ["sort_order"]
    list_filter = ['detail_category']


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'url', 'visible']
    search_fields = ['name']

    def get_queryset(self, request):
        return Employer.objects.distinct()


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'employer', 'date_start', 'date_end', 'visible']
    search_fields = ['employer__name']

    def get_queryset(self, request):
        return Employment.objects.distinct()


@admin.register(EmploymentTask)
class EmploymentTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'employment', 'name', 'sort_order']
    list_editable = ['sort_order']
    list_filter = ['employment__employer']
    search_fields = ['name', 'employment__employer__name']


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'sort_order']
    list_editable = ['sort_order']


@admin.register(HobbyItem)
class HobbyItemAdmin(admin.ModelAdmin):
    list_display = ['text', 'sort_order']
    list_editable = ['sort_order']


@admin.register(ExternalLink)
class ExternalLinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'fa_class', 'title', 'sort_index']
    list_editable = ['sort_index']
