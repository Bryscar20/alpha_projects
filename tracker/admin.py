from django.contrib import admin
from .models import Customer, TractorBrand, TractorModel, TractorDetails, Implement, OwnershipHistory

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'created_at', 'address')
    search_fields = ('first_name', 'email')

@admin.register(TractorBrand)
class TractorBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(TractorModel)
class TractorModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name')
    search_fields = ('brand',)
    list_filter = ('brand',)

@admin.register(TractorDetails)
class TractorAdmin(admin.ModelAdmin):
    list_display = ('registration_number','brand', 'model', 'chassis_number', 'engine_number', 'color', 'owner', 'updated_by')
    search_fields = ('registration_number', 'chassis_number', 'engine_number')
    list_filter = ('registration_number', 'chassis_number')

@admin.register(Implement)
class ImplementAdmin(admin.ModelAdmin):
    list_display = ('brand', 'chassis_number', 'color', 'owner', 'updated_by')
    search_fields = ('brand', 'chassis_number')
    list_filter = ('brand', 'owner')

@admin.register(OwnershipHistory)
class OwnershipHistoryAdmin(admin.ModelAdmin):
    list_display = ('tractor', 'implement', 'previous_owner', 'new_owner', 'change_date', 'updated_by')
    search_fields = ('tractor__registration_number', 'implement__chassis_number', 'previous_owner__first_name', 'new_owner__first_name')
    list_filter = ('change_date',)
