from django.db import models
from users.models import CustomUser
from products.models import Product

# Create your models here.
class Cart(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_of_products = models.PositiveIntegerField(default=0)
    num_of_items = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="carts")
    def update_totals(self):
        self.num_of_items = sum(item.quantity for item in self.cartitems.all())
        self.num_of_products = self.cartitems.count()
        self.total_price = sum(item.product.price *item.quantity for item in self.cartitems.all())
        self.save(update_fields=["num_of_products","num_of_items","total_price"])
    def __str__(self):
        return f"Cart-{self.user.username}-{self.created_at.date()}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cartitems")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="cartitems")
    quantity = models.PositiveIntegerField(default=1)
    def save(self,  *args, **kwargs):
        result = super().save( *args, **kwargs)
        self.cart.update_totals()
        return result
    def delete(self,  *args, **kwargs):
        cart = self.cart
        result = super().delete( *args, **kwargs)
        cart.update_totals()
        return result
     

    