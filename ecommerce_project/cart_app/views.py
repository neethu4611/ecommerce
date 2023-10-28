from django.shortcuts import render, redirect, get_object_or_404
from ecommerce_app.models import product
from cart_app.models import Cart,Cart_Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    products = product.objects.get(id=product_id)
    try:
         cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
         cart = Cart.objects.create(
            cart_id=_cart_id(request)
          )
         cart.save(),
    try:
        cart_item = Cart_Item.objects.get(products=products,cart=cart)
        if cart_item.quantity<cart_item.products.stock:
          cart_item.quantity += 1
          cart_item.save(),
    except Cart_Item.DoesNotExist:
        cart_item = Cart_Item.objects.create(
            products=products,
            quantity=1,
            cart=cart
        )
        cart_item.save(),

    return redirect('cart_app:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items= Cart_Item.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.products.price * cart_item.quantity)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))
def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    products=get_object_or_404(product,id=product_id)
    cart_item=Cart_Item.objects.get(products=products,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_app:cart_detail')

def fullremove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    products = get_object_or_404(product, id=product_id)
    cart_item = Cart_Item.objects.get(products=products, cart=cart)
    cart_item.delete()
    return redirect('cart_app:cart_detail')
