from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'stars', 'comment', 'created_at', 'updated_at')
    search_fields = ('movie', 'stars', 'comment')
    list_filter = ('movie', 'stars')
    list_per_page = 10
