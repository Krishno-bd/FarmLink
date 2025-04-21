from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm
from .forms import ReviewForm
from .models import Review

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('feedback:contact')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/contact.html', {'form': form})


# def add_review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user  # Link review to logged-in user
#             review.save()
#             return redirect('feedback:reviews')  # Redirect to the reviews list page
#     else:
#         form = ReviewForm()
    
#     return render(request, 'feedback/add_review.html', {'form': form})

# def reviews(request):
#     reviews = Review.objects.all()
#     return render(request, 'feedback/reviews.html', {'reviews': reviews})