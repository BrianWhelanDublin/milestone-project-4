from django.shortcuts import render


def view_blog(request):
    template = "blog/view_blog.html"

    return render(request,
                  template)
