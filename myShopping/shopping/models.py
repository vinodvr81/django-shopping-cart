# Create your models here.
from django.db import models
from datetime import datetime

class Cart(models.Model):
    shopping_list = models.JSONField(default=dict)
    purchased_date = models.DateTimeField("date purchased", auto_now_add=True)

# Example shopping list
shopping_data = {
    "items": [
        {"name": "apple", "quantity": 3},
        {"name": "banana", "quantity": 2},
        {"name": "bread", "quantity": 1},
        {"name": "rice", "quantity": 1}
    ]
}

# Create a new Cart object
cart = Cart.objects.create(
    shopping_list=shopping_data,
    purchased_date=datetime.now()
)

