from django.contrib import admin
from .models import studentdb

# Register your models here.
class Show(admin.ModelAdmin):
    list_display = ('ZYMC', 'XM', 'XB', 'KSH', 'XXMC')

admin.site.register(studentdb, Show)
