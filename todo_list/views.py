from .models import List
from .forms import ListForm
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Item added to the list"))
    items = List.objects.all
    return render(request, 'home.html', {'items': items})


def about(request):
    return render(request, 'about.html')


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item Delete from the List"))
    return redirect('home')


def cross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')
