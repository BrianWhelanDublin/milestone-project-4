from django.shortcuts import render, get_object_or_404
from .models import Post


def view_blog(request):
    posts = Post.objects.all()
    template = "blog/view_blog.html"
    context = {
        "posts": posts
    }

    return render(request,
                  template,
                  context)


def view_post(request, post_id):
    ''' Show the single post page '''

    post = get_object_or_404(Post, pk=post_id)

    template = "blog/post.html"

    context = {
        "post": post,
    }

    return render(request,
                  template,
                  context)
