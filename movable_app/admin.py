from django.contrib import admin
from .models import *

# Register your models here.
class OrnamentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition','is_confirm',)
admin.site.register(Ornaments , OrnamentsAdmin)    

class StocksAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(Stocks, StocksAdmin)

class ShareAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(Share, ShareAdmin)

class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(Insurance, InsuranceAdmin)

class Cash_or_bankvalueAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(Cash_or_bankvalue, Cash_or_bankvalueAdmin)

class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(Vehicles, VehiclesAdmin)

class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(Electronics, ElectronicsAdmin)

class Other_Admin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(Other_m, Other_Admin)

admin.site.register(NoteField)