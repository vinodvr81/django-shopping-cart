from django.shortcuts import render
from django.http import JsonResponse
from .models import Cart  # Ensure this import is AFTER Django setup
from datetime import datetime
import json

def cart_view(request):
    if request.method == "POST":
        shopping_list = request.POST.get("shopping_list", "{}")
        try:
            shopping_list_json = json.loads(shopping_list)
            cart = Cart.objects.create(shopping_list=shopping_list_json, purchased_date=datetime.now())
            return JsonResponse({"id": cart.id, "shopping_list": cart.shopping_list})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    carts = Cart.objects.all()
    return render(request, "cart.html", {"carts": carts})
