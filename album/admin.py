from django.contrib import admin
from album.models import Page

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Page, PageAdmin)
