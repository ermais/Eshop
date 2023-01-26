from django.shortcuts import render
from .models import Order,OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.

def order_create(request):
    cart = Cart(request)
    user = request.user
    if user != None:
        form = OrderCreateForm(initial={'first_name':user.first_name,'last_name':user.last_name,'email':user.email})

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(product=item['product'],
                order=order,price=item['price'],
                quantity=item['quantity'])
            cart.clear()
        return render(request,'order/created.html',{'order':order})

    return render(request,'order/create.html',{'cart':cart,'form':form})
