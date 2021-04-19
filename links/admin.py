from django.contrib import admin

from .models import LinkBoard, Link, SocialMedia


@admin.register(LinkBoard)
class LinkBoardAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'public_link')
    search_fields = ('user', 'public_link')
    list_display_links = ('user', 'title')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('board', 'whatsapp', 'telegram')


@admin.register(Link)
class LinkBoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'board')
