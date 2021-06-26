from django.contrib import admin

from chat.models import Chat, Message


@admin.register(Chat)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Message)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'chat']
