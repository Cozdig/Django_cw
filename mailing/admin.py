from django.contrib import admin
from .models import Recipient, Message, Mailings, MailingLog


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

@admin.register(Mailings)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'status')
    list_filter = ('start_time',)
    search_fields = ('start_time',)

@admin.register(MailingLog)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('status', 'error_message', 'attempt_time')
    list_filter = ('status',)
    search_fields = ('status',)

