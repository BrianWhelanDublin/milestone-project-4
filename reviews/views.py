from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from django.core.paginator import Paginator


def our_reviews(request):
    ''' renders all the reviews '''

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            form.save()

    reviews = Review.objects.all().order_by("-id")
    paginator = Paginator(reviews, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = ReviewForm()
    template = "reviews/our_reviews.html"
    context = {
        "form": form,
        "page_obj": page_obj,
    }

    return render(request,
                  template,
                  context)
