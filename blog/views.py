from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
#переход к странице post_detail после добавления новой записи
from django.contrib.auth.decorators import login_required

# Create your views here.
'''view, или представление, — это то место, где мы разместим «логику» работы нашего приложения. 
Оно запросит информацию из модели, которую мы создали ранее, и передаст её в шаблон'''

'''функция с именем post_list, которая принимает request в качестве аргумента и возвращает результат 
работы функции render, которая уже соберёт шаблон страницы
представления предназначены чтобы соединять между собой модели и шаблоны'''

def post_list(request): 
    #список записей блога, отсортированных по published_date
    #posts - имя для нашего QuerySet
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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
    return render(request, 'blog/post_edit.html', {'form': form})

'''def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})'''

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
    
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
    
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

'''The line posts = Post.objects.filter(published_date__isnull=True).order_by('created_date') 
makes sure that we take only unpublished posts (published_date__isnull=True) and order them by 
created_date (order_by('created_date')).'''

'''В функции render у нас уже есть параметр request (т.е. всё, что мы получим от пользователя в качестве 
запроса через Интернет) и файл шаблона 'blog/post_list.html'. Последний параметр, который выглядит как {},
 — это место, куда мы можем добавить что-нибудь для использования в шаблоне. Мы должны задавать имена 
 передаваемым шаблону вещам (прямо сейчас мы остановимся на 'posts' :)). В итоге параметр будет выглядеть 
 следующим образом: {'posts': posts}. Обрати внимание, что часть перед : является строкой; её нужно обернуть в кавычки ''.'''