"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import ListView
from cathegory.models import Cathegory
from . import views


urlpatterns = [

    url(r'^$',  ListView.as_view(queryset = Cathegory.objects.all()[:20], template_name = "cathegory/cathegories.html"), name='cathegories'),
    url(r'^(?P<pk>\d+)/$', views.cathegory_topics, name='cathegory_topics'),
    url(r'^(?P<pk>\d+)/new_topic$', views.new_topic, name='new_topic'),
    url(r'^(?P<cat_pk>\d+)/topics/(?P<pk>\d+)$', views.topic_posts, name='topic_posts'),
    url(r'^(?P<cat_pk>\d+)/topics/(?P<pk>\d+)/reply$', views.topic_reply, name='topic_reply'),


]
