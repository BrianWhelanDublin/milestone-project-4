from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from stock.models import Item
from users.models import UserProfile
from blog.models import Post

from .forms import NewsletterForm, MessageForm


def home_page(request):
    ''' retrieve the new items from the databse,
        then render the homepage'''

    new_items = Item.objects.filter(category=7)
    posts = Post.objects.all().order_by("-id")[:3]

    if request.method == "POST":
        subscribers_email = request.POST["email"]
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = render_to_string(
                "homepage/newsletter/newsletter_subject.txt"
            )
            body = render_to_string(
                "homepage/newsletter/newsletter_content.txt"
            )
            send_mail(
                subject,
                body,
                settings.DEFAULT_EMAIL_ADDRESS,
                [subscribers_email]
            )
            messages.success(request,
                             "You have been signed up for our newsletter")
            form.save()
            return redirect("home_page")
        else:
            messages.error(request,
                           "Something has gone wrong.\
 Please check your email address and try again.")
            return redirect("home_page")
    else:
        form = NewsletterForm()

    template = "homepage/index.html"
    context = {
        "new_items": new_items,
        "form": form,
        "posts": posts,
    }

    return render(request,
                  template,
                  context)


def our_story(request):
    ''' render our story page '''

    template = "homepage/our_story.html"

    return render(request,
                  template)


def contact(request):
    ''' renders the contact us page '''
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Your message has been sent.\
 A member of our customer service team will be in contact soon.")
            return redirect("home_page")
        else:
            messages.error(request,
                           "Something has gone wrong.\
 Please try again soon")
            return redirect("contact")
    else:
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                form = MessageForm(initial={
                    "user_email": user_profile.user.email
                })
            except UserProfile.DoesNotExist:
                form = MessageForm()
        else:
            form = MessageForm()

    template = "homepage/contact.html"
    context = {
        "form": form,
    }

    return render(request,
                  template,
                  context)
