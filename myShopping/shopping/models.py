# Create your models here.
from django.db import models
from datetime import datetime

class Cart(models.Model):
    shopping_list = models.JSONField(default=dict)
    purchased_date = models.DateTimeField("date purchased", auto_now_add=True)


