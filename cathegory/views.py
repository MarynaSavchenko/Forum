from django.shortcuts import render
from django.http import Http404
from .models import Topic, Cathegory

# Create your views here.

def cathegory_topics(request, pk):

    try:
        cathegory = Cathegory.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404

    return render(request, 'cathegory/topics.html', {'cathegory':cathegory})
