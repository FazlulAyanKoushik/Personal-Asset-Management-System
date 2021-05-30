from django.contrib import admin
from .models import Designation, Profile, Messsage

# Register your models here.
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Designation, DesignationAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','designation', 'gender',)  

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Messsage)