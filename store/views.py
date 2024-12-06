from django.shortcuts import render
from .models import Category, Product

# Home view
def home(request):
    ctg = Category.objects.all()  # Corrected this line
    product = Product.objects.all()
    ctx = {
        'ctg': ctg,
        'product': product
    }
    return render(request,'index.html', ctx)

def contact(request):
    ctx = {}
    return render(request,'contact.html', ctx)

# Products view
def products(request, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)  # Corrected this line
    product = Product.objects.filter(type_id=category.id)  # Corrected this line
    ctx = {
        'ctg': ctg,
        'category': category,
        'product': product
    }
    return render(request,'products.html', ctx)

# Register view
def register(request):
    ctx = {}
    return render(request,'register.html', ctx)

# Single product view
def single(request):
    ctx = {}
    return render(request,'single.html', ctx)
