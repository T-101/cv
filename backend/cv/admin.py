from django.contrib import admin
from django.utils.html import format_html

from .models import Email, PhoneNumber, Picture, PersonalInfo, DetailCategory, DetailItem, Employer, Employment, \
    EmploymentTask, Hobby, HobbyItem, ExternalLink, PortfolioItem, PortfolioImage, PortfolioItemTag, PortfolioTechniques


# InLines

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1


# Admins

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


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    change_form_template = "admin/cv/markdown_change_form.html"
    list_display = ['id', 'title', 'visible']
    list_filter = ['visible']
    search_fields = ['title', 'description', "tags__tag", "techniques__technique"]
    autocomplete_fields = ['tags', 'techniques']
    inlines = [PortfolioImageInline]
    readonly_fields = ['slug', 'description_preview']

    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'short_description', 'description', 'description_preview',
                       'techniques', 'tags', 'url', 'url_type', 'repository', 'visible', 'slug')
        }),
    )

    def description_preview(self, obj):
        return format_html("<div id='description_preview'</div>")


@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    search_fields = ['item__title']


@admin.register(PortfolioItemTag)
class PortfolioItemTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']
    search_fields = ['tag']


@admin.register(PortfolioTechniques)
class PortfolioTechniquesAdmin(admin.ModelAdmin):
    list_display = ['id', 'technique']
    search_fields = ['technique']
