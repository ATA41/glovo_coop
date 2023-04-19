from django.shortcuts import render


from django.http import HttpResponse

from .models import *

def index(request):
    return HttpResponse("index")

def orders(request):
    orders_all = Order.objects.all()
    return render(request, "orders.html", {"orders": orders_all})
