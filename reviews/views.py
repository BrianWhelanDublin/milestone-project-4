from django.shortcuts import render


def our_reviews(request):
    ''' renders all the reviews '''

    template = "reviews/our_reviews.html"

    return render(request,
                  template)
