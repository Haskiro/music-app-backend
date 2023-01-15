import imp
from django.contrib import admin
from track.models import Track
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Track)
class TrackAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ["title", "released_at"]
    ordering = ('?',)
    list_filter = ['artist']
    search_fields = ("title__startswith", )
    fields = ("title", "audio_file", "cover", "released_at", "artist")
