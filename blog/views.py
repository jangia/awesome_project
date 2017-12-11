from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from blog.models import Post


def posts(request):

    all_posts = Post.objects.all()
    params = {
        'posts': all_posts
    }

    return render(request, 'blog.html', context=params)


@login_required
def single_post(request, pk):

    post = Post.objects.get(pk=pk)

    params = {
        'post': post
    }

    return render(request, 'single_post.html', context=params)