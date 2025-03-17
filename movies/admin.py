from django.contrib import admin
from movies.models import Movies

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'resume', 'created_at', 'updated_at')
    search_fields = ('title', 'genre', 'actors')
    list_filter = ('genre', 'actors')
    list_per_page = 10
