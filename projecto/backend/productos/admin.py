from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display =  ['nombre', 'valor', 'fecha', 'created_at']
    list_filter = ['fecha', 'created_at']
    search_fields = ['nombre']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
