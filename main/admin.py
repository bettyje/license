from django.contrib import admin
from .models import License, LicenseCategory


class LicenseInline(admin.TabularInline):
    model = License
    extra = 1
    fields = ('name', 'address', 'license_number', 'weblink')
    show_change_link = True   # lets you click through to edit License


@admin.register(LicenseCategory)
class LicenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)   # assuming LicenseCategory has a name field
    search_fields = ('name',)
    inlines = [LicenseInline]


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'address', 'weblink', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'address', 'license_number', 'category__name')
    ordering = ('name',)
