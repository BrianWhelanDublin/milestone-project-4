from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required


def view_blog(request):
    ''' A view to show the blog page '''

    posts = Post.objects.all()
    template = "blog/view_blog.html"
    context = {
        "posts": posts,
    }

    return render(request,
                  template,
                  context)


def view_post(request, post_id):
    ''' Show the single post page and
        the comments and comments form to logged in users
    '''

    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            form.save()
            messages.success(request, "Your comment has been added.")
            return redirect(reverse("view_post", args=[post_id]))
        else:
            messages.error(request,
                           "Error adding your comment please try again")
            return redirect(reverse("view_post", args=[post_id]))
    comments = Comment.objects.filter(post=post)

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


@login_required
def delete_comment(request, post_id):
    '''  A view to delete a users comment
         Will also show an error msg if a user tries type
         the url into the browser.
    '''

    if request.method == "POST":
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


@login_required
def add_post(request):
    ''' A view to allow superusers to add a new blog post
        from the front end of the website. If a user types the
        url into the browser they will get an error message.
    '''

    if request.user.is_superuser:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, "Post has been added successfully.")
                return redirect(reverse("view_post", args=[post.id]))
            else:
                messages.error(request,
                               "Failed to add the post. \
Please check the form details are correct and try again.")
        else:
            form = PostForm()
    else:
        messages.error(request, "You do not have permission to do this.")
        return redirect(reverse("view_blog"))
    template = "blog/add_post.html"
    context = {
        "form": form,
    }

    return render(request,
                  template,
                  context)


@login_required
def edit_post(request, post_id):
    ''' A view to allow the super user to edit a post
        from the front end of the website. It will also
        give an error msg if the user tries to type the url
        into the browser.
    '''

    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=post_id)
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 "Post updated successfully")
                return redirect(reverse("view_post", args=[post.id]))
            else:
                messages.error(request,
                               "Failed to edit the post. \
Please check the form details are correct and try again.")
        else:
            form = PostForm(instance=post)
    else:
        messages.error(request, "You do not have permission to do this.")
        return redirect(reverse("view_blog"))

    template = "blog/add_post.html"
    context = {
        "form": form,
        "post": post,
        "edit_post": True,
    }

    return render(request,
                  template,
                  context)


@login_required
def delete_post(request, post_id):
    ''' view to delete a post from the front end of
        the website also gives an error message if the
        user types the url into the browser
        '''

    if request.user.is_superuser:
        if request.method == "POST":
            post = get_object_or_404(Post, pk=post_id)
            post.delete()
            messages.success(request, "Post has been deleted")
            return redirect(reverse("view_blog"))
        else:
            messages.error(request, "You do not have permission to do this.")
            return redirect(reverse("view_blog"))
    else:
        messages.error(request, "You do not have permission to do this.")
        return redirect(reverse("view_blog"))
