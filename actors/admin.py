from django.contrib import admin
from actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date', 'nationality', 'active', 'created_at')
    search_fields = ('name',)
    list_filter = ('active', 'nationality')