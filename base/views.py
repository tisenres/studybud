from django.shortcuts import render

from base.models import Room


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(pk=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
