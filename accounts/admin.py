from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm , UserChangeForm
from .models import EmailConfirmed

# Register your models here.
User = get_user_model()

admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    list_display = ('email','name', 'user_type','date', 'phone_no', 'is_active', 'is_admin', 'is_staff',)
    list_filter = ('is_admin',)

    fieldsets = (
        (
            None, {
                'fields': ('name', 'email','user_type', 'phone_no', 'password')
            }
        ),
        (
            'permissions', {
                'fields': ('is_active', 'is_admin', 'is_staff')
            }
        )
    )

    add_fieldsets = (
        (
            None, {
                'fields': ('name','email','user_type','date', 'phone_no', 'is_active', 'password1', 'password2')
            }
        ),
        (
            'permissions', {
                'fields': ('is_active','is_admin', 'is_staff')
            }
        )
    )

    ordering = ('email',)
    search_fields = ('email', 'phone_no',)
    filter_horizontal = ()

admin.site.register(User , UserAdmin)

class EmailConfirmedAdmin(admin.ModelAdmin):
    """ class docstring """
    list_display = ('user', 'name', 'activation_key', 'email_confirmed')

    def name(self, obj):
        return obj.user.name

admin.site.register(EmailConfirmed, EmailConfirmedAdmin)        

