from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
  return render(request, 'chats/index.html')


def room(request,roomid):
  username = request.GET.get('username')
  rooms = Room.objects.get(name=roomid)
  context={
    'username':username,
    'rooms':rooms
  }
  return render(request, 'chats/room.html', context)


def checkroom(request):
  room = request.POST['room']
  username = request.POST['username']
  
  if Room.objects.filter(name=room).exists():
    return redirect('/'+room+'/?username='+ username)
  else:
    new_room = Room.objects.create(name=room)
    new_room.save()
    return redirect('/'+room+'/?username='+ username)


def send(request):
  rooms = request.POST['rooms']
  username = request.POST['username']
  msg = request.POST['msg']

  messages = Message.objects.create(msg = msg, user =username, room = rooms)
  messages.save()
  return HttpResponse('Message Sent Successfully !')

def messages(request, roomid):
  room = Room.objects.get(name=roomid)
  msgs = Message.objects.filter(room = room.id)
  return JsonResponse({'messages': list(msgs.values())})
