from django.contrib import admin
from .models import *

# Register your models here.
class LandAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition','is_confirm',)
admin.site.register(Land , LandAdmin)    

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(Building, BuildingAdmin)

class HomesteadAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(Homestead, HomesteadAdmin)

class BusinessFirmAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(BusinessFirm, BusinessFirmAdmin)

class OtherAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner', 'date_of_acquisition', 'is_confirm',)
admin.site.register(Other, OtherAdmin)

admin.site.register(NoteField_im)

