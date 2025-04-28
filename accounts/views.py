from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import ProfileForm, NewsletterSignupForm
from orders.models import Order


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )
    orders = Order.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your profile has been updated successfully!"
            )
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'accounts/profile.html', {
        'form': form,
        'orders': orders,  # Pass orders to the template
    })


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for subscribing to our newsletter!'
            )
            return redirect('home')
    else:
        form = NewsletterSignupForm()
    return render(request, 'accounts/newsletter_signup.html', {'form': form})
