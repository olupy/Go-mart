from django.db import models
from django.contrib.auth.models import User
# Create your models here.

LABEL = (('NEW','N'),('TRENDING','T'),('BEST_SELLER','BS'))

class Category(models.Model):
    category_name = models.CharField(blank = True, max_length= 30)

    def __str__(self) -> str:
        return f"{self.category_name}"

class Item(models.Model):
    item_name = models.CharField(max_length= 40)
    price = models.FloatField(blank = False)
    discount_price = models.FloatField(null = True, blank = True)
    category = models.ForeignKey(Category,null = True, on_delete=models.SET_NULL)
    label = models.CharField(choices = LABEL, null = True, blank = True, max_length=20)
    description = models.TextField(max_length= 600)
    image = models.ImageField(upload_to ='Item', null = True)

    def __str__(self) -> str:
        return f"{self.item_name}"

class OrderItem(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    ordered = models.BooleanField(default = False)
    item = models.ForeignKey(Item,null= True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default = 1)
    
    def __str__(self) -> str:
        return f"{self.quantity} of {self.item.item_name}"

class Order(models.Model):
    user = models.ForeignKey(User,related_name = 'user_order',null = True, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem, related_name = 'items_ordered')
    start_date = models.DateTimeField(auto_now_add= True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default = False)

def __str__(self):
    return self.user.username
