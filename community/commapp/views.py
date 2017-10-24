from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Coms, Post
from .forms import PostForm
from django.shortcuts import redirect


def index(request):
    coms = Coms.objects.order_by('category')
    cats = Coms.objects.values('category').distinct()
    return render(request,'index.html', {'coms':coms, 'cats':cats})

def community(request, pk):
    com = Post.objects.filter(group=pk)
    return render(request, 'community.html', {'com': com})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('community', group=pk)
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})

def calendar(request):
    return render(request, 'calendar.html')
