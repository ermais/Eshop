from django.db import models
from product.models import Product

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(null=False,blank=False,max_length=60)
    last_name = models.CharField(null=False,blank=False,max_length=60)
    email = models.EmailField(null=False,blank=False)
    address = models.CharField(max_length=120,null=False,blank=False)
    postal_code = models.CharField(max_length=60,null=False,blank=False)
    city = models.CharField(max_length=60,null=False,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=True)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


    def __str__(self):
        return f"{self.city}, {self.address} ordered by {self.first_name} {self.last_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product =models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items')
    price = models.DecimalField(max_digits=12,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.product.name}"

    def get_cost(self):
        return self.price * self.quantity


