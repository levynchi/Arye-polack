from django.contrib import admin
from .models import Performance, Track, ContactMessage


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'has_audio')
    list_filter = ('year',)
    search_fields = ('title',)
    fields = ('title', 'audio_file', 'year', 'description')

    def has_audio(self, obj):
        return bool(obj.audio_file)
    has_audio.boolean = True
    has_audio.short_description = 'קובץ אודיו'


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'date')
    list_filter = ('date',)
    ordering = ('date',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
