from django.shortcuts import render
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from stock.models import Item

from .forms import NewsletterForm


def home_page(request):
    ''' retrieve the new items from the databse,
        then render the homepage'''

    new_items = Item.objects.filter(category=7)

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
        else:
            messages.error(request,
                           "Something has gone wrong.\
 Please check your email address and try again.")

    form = NewsletterForm()

    template = "homepage/index.html"
    context = {
        "new_items": new_items,
        "form": form,
    }

    return render(request,
                  template,
                  context)


def our_story(request):
    ''' render our story page '''

    template = "homepage/our_story.html"

    return render(request,
                  template)
