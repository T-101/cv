from django.contrib import admin

from cv.models import Employer, Employment, EmploymentTask


class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url', 'visible')
    list_filter = ('visible', 'name')
    search_fields = ('name', 'description', 'url')


admin.site.register(Employer, EmployerAdmin)


class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('employer', 'date_start', 'date_end', 'visible')
    list_filter = ('visible', 'employer__name')


admin.site.register(Employment, EmploymentAdmin)


class EmploymentTaskAdmin(admin.ModelAdmin):
    list_display = ('employment', 'name')


admin.site.register(EmploymentTask, EmploymentTaskAdmin)
