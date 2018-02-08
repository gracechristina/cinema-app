from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post, Movies
from .forms import PostForm, MoviesForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  
from django.views.generic import FormView

def post_list(request):
    posts = Post.objects.filter().order_by('published_date')
    return render(request, 'cinema/post_list.html', {'posts': posts})



def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'cinema/post_detail.html',{'post':post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'cinema/post_edit.html', {'form': form})

@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)
    return render(request, 'cinema/post_edit.html',{'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'cinema/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


class MoviesPage(FormView):  
    template_name = 'cinema/movies.html'
    success_url = '/awesome/'
    form_class = MoviesForm

    def form_valid(self, form):
        return redirect('movie_detail')

def movies(request):
    posts = Post.objects.filter().order_by('published_date')
    return render(request, 'cinema/movies.html', {'movies': movies})

def movie_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'cinema/movie_detail.html',{'movies':movies})
