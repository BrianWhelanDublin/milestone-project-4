from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def user_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    template = "users/user_profile.html"

    form = UserProfileForm(instance=profile)

    context = {
        "form": form,
    }

    return render(request,
                  template,
                  context)
