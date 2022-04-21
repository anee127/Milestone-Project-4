from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


@login_required
def add_review(request, product_id):
    """
    Allow user to add a review
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form = review_form.save(commit=False)
            review_form.product = product
            review_form.user = user
            review_form.save()
            messages.success(request, 'Thank you! Your review has been added')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Something went wrong. '
                                    'Make sure the form is valid.')
    else:
        review_form = ReviewForm()
    template = 'reviews/reviews.html'
    context = {
        'review_form': review_form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """
   form edited by user
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            # Success message if added
            messages.success(
                request, 'Thank You! Your review has been updated!')
            return redirect(
                reverse('product_detail', args=(review.product.id,)))
        else:
            # Error message if form was invalid
            messages.error(request, 'Something went wrong. '
                                    'Make sure the form is valid.')
    else:
        review_form = ReviewForm(instance=review)

    template = "reviews/reviews.html"
    context = {
        "review_form": review_form,
        "review": review,
        "product": review.product,
    }

    return render(request, template, context)


def delete_review(request, review_id):
    """
    Deletes user's review
    """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Your review was deleted')

    return redirect(reverse('product_detail', args=(review.product.id,)))
