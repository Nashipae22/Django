from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name
    
class Products (models.Model):
    name= models.CharField(max_length=100)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description= models.TextField()
    stock=models.PositiveIntegerField(default=0)
    img=models.ImageField(upload_to='media/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        return f"Order {self.id} by {self.user.username} - ${self.total_price}"
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product= models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
    
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart for {self.user.username}"

    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product= models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart"
    
class Payment(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    amount=models.IntegerField()
    payment_method=models.CharField(max_length=50)
    payment_status=models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.id} for Order {self.order.id} - {self.amount}"
    
class ShipAddress(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address_1=models.CharField(max_length=250)
    address_2=models.CharField(max_length=250)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Address for {self.user.username}: {self.address_line1}, {self.city}, {self.country}"
    
class Review(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    rating=models.PositiveIntegerField()
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name} - Rating: {self.rating}"







    

    
        

    