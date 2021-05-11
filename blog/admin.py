from django.contrib import admin
from .models import  Categorias, Post
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    #campos de solo lectura
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    #campos de solo lectura
    readonly_fields = ('created', 'updated')


admin.site.register(Categorias, CategoriaAdmin)
admin.site.register(Post,PostAdmin)