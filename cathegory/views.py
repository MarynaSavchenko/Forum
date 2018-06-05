from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Cathegory, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm

# Create your views here.

def cathegory_topics(request, pk):

    cathegory = get_object_or_404(Cathegory, pk=pk)
    return render(request, 'cathegory/topics.html', {'cathegory':cathegory})


def new_topic(request, pk):

    cathegory = get_object_or_404(Cathegory, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':

        form = NewTopicForm(request.POST)
        if form.is_valid():

            topic = form.save(commit = False)
            topic.cathegory = cathegory
            topic.creater = user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                creater = user
            )

        return redirect('cathegory_topics', pk=cathegory.pk)  # TODO: redirect to the created topic page

    else:
        
        form = NewTopicForm()

    return render(request, 'cathegory/new_topic.html', {'cathegory':cathegory, 'form':form})
