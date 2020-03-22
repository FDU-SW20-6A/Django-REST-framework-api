from django.contrib import admin
from .models import pos
# Register your models here.

@admin.register(pos)
class  posAdmin(admin.ModelAdmin):
    pass