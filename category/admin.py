from django.contrib import admin
from models import Category

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'description']
    class Meta:
        model = Category


admin.site.register(Category, CategoryModelAdmin)