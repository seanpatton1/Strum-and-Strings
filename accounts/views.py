from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Order
from .forms import ProfileForm


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    orders = Order.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'accounts/profile.html', {
        'form': form,
        'orders': orders,
    })
