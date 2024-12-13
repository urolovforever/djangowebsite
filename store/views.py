from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Buy
from .forms import ChoiceForm


# Home view
def home(request):
    ctg = Category.objects.all()  # Get all categories
    product = Product.objects.all()  # Get all products
    ctx = {
        'ctg': ctg,
        'product': product
    }
    return render(request, 'index.html', ctx)


def contact(request):
    ctx = {}
    return render(request, 'contact.html', ctx)


# Products view
def products(request, slug=None):
    ctg = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)  # Handle category not found
    product = Product.objects.filter(type_id=category.id)  # Filter products by category
    ctx = {
        'ctg': ctg,
        'category': category,
        'product': product
    }
    return render(request, 'products.html', ctx)


# Register view
def register(request):
    ctx = {}
    return render(request, 'register.html', ctx)


# Single product view
def single(request, pk=None):
    ctg = Category.objects.all()

    # Get the product or return 404 if not found
    product_pk = get_object_or_404(Product, pk=pk)

    # Initialize the form
    if request.method == 'POST':
        form = ChoiceForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the form data but don't commit to the database yet
            root = form.save(commit=False)

            # Associate the 'product' field with the selected product
            root.product = product_pk

            # Save the object to the database
            root.save()

            # Redirect to home page after successful form submission
            return redirect('home')
        else:
            # If the form is not valid, print errors
            print(form.errors)
    else:
        # If it's a GET request, display the form
        form = ChoiceForm()

    # Ensure a response is always returned, even for GET requests
    return render(request, 'single.html', {'form': form, 'ctg': ctg, 'product': product_pk})
