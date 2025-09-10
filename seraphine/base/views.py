from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Cadastro'},
    {'id': 2, 'name': 'Login'},
    {'id': 3, 'name': 'chat'}
]

def landing(request):
    return render(request, 'base/landing.html', {'rooms': rooms})

def chat(request, pk):
    chat = None
    for i in rooms:
        if i['id'] == int(pk): 
            chat = i
    context = {'chat': chat}
    return render(request, 'base/chat.html', context)