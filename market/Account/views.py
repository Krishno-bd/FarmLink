from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(request, 'Account Created Successfully', extra_tags="success")
            return redirect('Account:signin')
        else:
            messages.error(request, 'Unsuccessful Registration', extra_tags="error")

    form = RegistrationForm()
    return render(request, 'Account/signup.html', {'form': form})


@login_required
def profile(request):
    # Ensure the profile exists
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'Account/profile.html', {'profile': profile})

@login_required
def update_profile(request):
    user = request.user  # No need for get_or_create here; request.user always exists
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!', extra_tags="success")
            return redirect('Account:profile')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'Account/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
