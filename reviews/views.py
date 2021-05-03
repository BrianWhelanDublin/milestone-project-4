from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
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
            review.stars = int(request.POST.get("stars"))
            review.save()

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


def edit_review(request, review_id):
    ''' View to edit a users review '''

    review = get_object_or_404(Review, pk=review_id)
    if review.reviewer != request.user:
        messages.error(request,
                       "You do not have permission to do this.")
        return redirect(reverse("our_reviews"))
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.stars = int(request.POST.get("stars"))
            review.save()
            messages.success(request,
                             "Review has been updated.")
            return redirect(reverse("our_reviews"))
        else:
            messages.error(request,
                           "Failed to update review. Please try again later.")
    else:
        form = ReviewForm(instance=review)

    reviews = Review.objects.all().order_by("-id")
    paginator = Paginator(reviews, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = "reviews/our_reviews.html"
    context = {
        "form": form,
        "page_obj": page_obj,
        "edit_review": True,
        "review_to_edit": review,
    }

    return render(request,
                  template,
                  context)


def delete_review(request, review_id):
    ''' View to delete a review '''

    review = get_object_or_404(Review, pk=review_id)
    if review.reviewer != request.user:
        messages.error(request,
                       "You do not have permission to do this.")
        return redirect(reverse("our_reviews"))

    if request.method == "POST":
        review.delete()
        messages.success(request,
                         "Review has been deleted")
        return redirect(reverse("our_reviews"))
    else:
        messages.error(request,
                       "You do not have permission to do this.")
        return redirect(reverse("our_reviews"))
