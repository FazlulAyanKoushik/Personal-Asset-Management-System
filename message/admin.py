from django.contrib import admin
from .models import InboxMessage,  NewMessage

admin.site.register(InboxMessage)
admin.site.register(NewMessage)