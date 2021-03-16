from django.shortcuts import render
from .forms import ReviewForm
from .models import Review


from django.contrib.auth.decorators import login_required


@login_required
def our_reviews(request):
    ''' renders all the reviews '''
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.reviewer = request.user
                form.save()
    form = ReviewForm()
    template = "reviews/our_reviews.html"
    context = {
        "form": form,
    }

    return render(request,
                  template,
                  context)
