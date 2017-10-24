from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Coms, Post
from .forms import PostForm


def index(request):
    coms = Coms.objects.order_by('category')
    cats = Coms.objects.values('category').distinct()
    return render(request,'index.html', {'coms':coms, 'cats':cats})

def community(request, pk):
    com = Post.objects.filter(group=pk)
    return render(request, 'community.html', {'com': com})

def new_post(request):
    form = PostForm()
    return render(request, 'new_post.html', {'form': form})
