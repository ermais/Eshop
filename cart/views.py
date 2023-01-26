from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST,require_http_methods
from .forms import AddToCartForm, UpdateCartForm
from .cart import Cart
from django.http import JsonResponse
from product.models import Product

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
# Create your views here.
@require_http_methods(["GET","POST"])
def add_cart(request):
    cart = Cart(request)
    if request.method == 'POST' and is_ajax(request):
            print("Request is ajax request")
            print(dir(request.META.get('HTTP_X_REQUESTED_WIDTH')))
            form = AddToCartForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                product = Product.objects.get(pk=cd['product_id'])
                cart.add(product,quantity=1,override_quantity=True)
                cart_items = len(cart)
                return JsonResponse({'cart_items':cart_items})

                return 
    print(False)
    return redirect('product_list')

@require_http_methods(["GET","POST"])
def remove_from_cart(request):
    cart = Cart(request)
    if request.method == 'POST' and is_ajax(request):
        print('----------------------')
        print(request.headers)
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            product = Product.objects.get(pk=cd['product_id'])
            cart.remove(product)
            cart_items = len(cart)
            return JsonResponse({'cart_items':cart_items})
    print(False)
    return redirect('product_list')

def cart_view(request):
    cart = Cart(request)
    if request.method == 'POST' and is_ajax(request):
        form = UpdateCartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            product=Product.objects.get(pk=cd['product'])
            cart.add(product=product,quantity=cd['quantity'],override_quantity=True)

            return JsonResponse({'item':cd['quantity'],'price':15000,'cart_items':len(cart)})
    for item in cart:
        item['update_cart_form'] = UpdateCartForm(initial={'product':item['product'].id,'quantity':item['quantity']})
    return render(request,'cart/cart_detail.html',{'cart':cart})