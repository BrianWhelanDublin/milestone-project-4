from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def user_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    template = "users/user_profile.html"

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Your profile has been updated successfully.")

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        "form": form,
        "on_profile_page": True,
        "orders": orders,
    }

    return render(request,
                  template,
                  context)


def previous_order(request):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, "This is a previous order")

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "previous_order": True,
    }

    return render(request,
                  template,
                  context)
