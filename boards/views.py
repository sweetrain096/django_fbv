from django.shortcuts import render
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards' : boards}
    return render(request, 'boards/index.html', context)