from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Cathegory, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm, PostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

def cathegory_topics(request, pk):

    cathegory = get_object_or_404(Cathegory, pk=pk)
    return render(request, 'cathegory/topics.html', {'cathegory':cathegory})

@login_required
def new_topic(request, pk):

    cathegory = get_object_or_404(Cathegory, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.cathegory = cathegory
            topic.creater = request.user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                creater = request.user
            )
            return redirect('topic_posts', cat_pk = cathegory.pk, pk = topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'cathegory/new_topic.html', {'cathegory': cathegory, 'form': form})

def topic_posts(request, cat_pk, pk):

    topic = get_object_or_404(Topic, cathegory__pk =cat_pk, pk = pk)
    topic.views+=1
    topic.save()
    return render(request, 'cathegory/topic_posts.html', {'topic' : topic})

@login_required
def topic_reply(request, cat_pk, pk):

    topic = get_object_or_404(Topic, cathegory__pk =cat_pk, pk = pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.topic = topic
            post.creater = request.user
            post.save()
            topic.last_updated = timezone.now()
            topic.save()
            return redirect('topic_posts', cat_pk = cat_pk, pk = pk)
    else:
        form = PostForm()
    return render(request, 'cathegory/reply_topic.html', {'topic' : topic, 'form' : form})
