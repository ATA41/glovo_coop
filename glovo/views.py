from django.shortcuts import render

from .models import Order


def orders(request):
    orders_all = Order.objects.all()
    return render(request, "orders.html", {"orders": orders_all})
