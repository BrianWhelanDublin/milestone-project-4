from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


def view_blog(request):
    posts = Post.objects.all()
    template = "blog/view_blog.html"
    context = {
        "posts": posts,
    }

    return render(request,
                  template,
                  context)


def view_post(request, post_id):
    ''' Show the single post page '''
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            form.save()
            messages.success(request, "Your comment has been added.")
    comments = Comment.objects.all().order_by("-id")

    form = CommentForm()
    template = "blog/post.html"

    context = {
        "form": form,
        "post": post,
        "comments": comments,
    }

    return render(request,
                  template,
                  context)


def delete_comment(request, post_id):
    if request.method == "POST":
        # comment_id = request.POST["comment_id"]
        # print(comment_id)
        try:
            comment = get_object_or_404(
                Comment, pk=request.POST["comment_id"])
            comment.delete()
            messages.success(request, "Your comment has been deleted.")
            return redirect(reverse("view_post", args=[post_id]))
        except Exception as error:
            messages.error(request, "Error deleteing your comment")
            return redirect(reverse("view_post", args=[post_id]))
    else:
        messages.error(request, "Error you do not have \
permission to do this.")
        return redirect(reverse("view_post", args=[post_id]))
