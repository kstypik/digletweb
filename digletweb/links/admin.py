from digletweb.links.models import Link
from django.contrib import admin


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "description", "domain", "author", "created"]
    date_hierarchy = "created"
    raw_id_fields = ["author"]
    search_fields = ["title", "description", "domain"]
