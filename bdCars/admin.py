from django.contrib import admin
from .models import Car, Company, Owner, Country
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("model",)}
    list_filter = ("company", "used",)
    list_display = ("model", "company",)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name",)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ("name",)


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code",)


admin.site.register(Car, CarAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Country, CountryAdmin)
