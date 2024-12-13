from django.contrib import admin
from .models import *
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, ClientAdmin)
admin.site.register(Product, ClientAdmin)

admin.site.register(Buy)