from django.contrib import admin
from .models import Recipient, Message


# Register your models here.
@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('email', 'fullname', 'comment')
    list_filter = ('email', )
    search_fields = ('fullname', 'comment',)

@admin.register(Message)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('topic', 'content')
    list_filter = ('topic', )
    search_fields = ('topic',)