from django.shortcuts import render
from django.http import HttpResponse

from add.forms import PlayerForm

# Create your views here.

def index(request):
    return HttpResponse("Hello World")


def playerTracker(request):
    print('Working')
    if request.method == 'POST':
        form = PlayerForm(request.POST)

        if form.is_valid():
         print('VALID')
         form.save()

    form = PlayerForm()
    return render(request, 'player.html', {'form' : form})