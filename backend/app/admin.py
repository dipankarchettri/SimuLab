from django.contrib import admin
from .models import Topic

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'created_at')
    list_filter = ('category', 'subcategory')  # Filter by category and subcategory

admin.site.register(Topic, TopicAdmin)
