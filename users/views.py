from django.shortcuts import render


def user_profile(request):
    template = "users/user_profile.html"
    context = {}

    return render(request,
                  template,
                  context)
