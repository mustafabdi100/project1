from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def product(request):
    product = Product.objects.all()
    return render(request, 'product.html', {'product': product})
