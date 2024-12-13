from django.contrib import admin
from .models import Category, Product, Buy


# Register the models with the admin site
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Buy)

