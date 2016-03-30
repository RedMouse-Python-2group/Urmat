from django.shortcuts import render
from django.views.generic import ListView

from menu.models import Menu

# Create your views here.

class MenuList(ListView):
    model = Menu
    template_name="menu/menu.html"