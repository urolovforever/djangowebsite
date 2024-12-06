from django.contrib import admin
from .models import Category, Product


# Register the models with the admin site
admin.site.register(Category)
admin.site.register(Product)
