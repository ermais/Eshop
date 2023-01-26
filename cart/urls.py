from django.urls import path
from .views import add_cart,remove_from_cart,cart_view

urlpatterns = [
    path("add/",add_cart, name="add_cart"),
    path("remove/",remove_from_cart,name="remove_from_cart"),
    path("",cart_view,name="cart_detail"),
]
