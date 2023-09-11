from django.shortcuts import get_object_or_404, render

from productapp.models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request,"productapp/product_list.html",{'products':products})

def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'/home/sudhakarreddy/Djangoprojects/project5/productapp/templates/productapp/product_detail.html',{'product':product})




















