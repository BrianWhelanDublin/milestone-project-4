from django.shortcuts import render
from .forms import ReviewForm




def our_reviews(request):
    ''' renders all the reviews '''
    form = ReviewForm()
    template = "reviews/our_reviews.html"
    context = {
        "form": form,
    }

    return render(request,
                  template,
                  context)
