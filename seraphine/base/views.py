from django.shortcuts import render
from .models import Chat

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Cadastro'},
#     {'id': 2, 'name': 'Login'},
#     {'id': 3, 'name': 'chat'}
# ]

def landing(request):
    rooms = Chat.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/landing.html', {'rooms': rooms})

def chat(request, pk):
    chat = Chat.objects.get(id=pk)
    context = {'chat': chat}
    return render(request, 'base/chat.html', context)