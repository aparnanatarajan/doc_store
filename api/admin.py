from django.contrib import admin

from .models import Document, Folder, Topic


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "file",)


class FolderAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


admin.site.register(Document, DocumentAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(Topic, TopicAdmin)
