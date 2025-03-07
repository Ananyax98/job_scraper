# Copy this code to admin.py
from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'scraped_date')
    search_fields = ('title', 'company', 'location')
    list_filter = ('scraped_date', 'location')