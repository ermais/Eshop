from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import UserProfileUpdate

# Create your views here.
def user_profile_update(request):
    if request.method == 'POST':
        user_profile_update = UserProfileUpdate(data=request.POST)
        if user_profile_update.is_valid():
            user_profile_update.save()
            return redirect(reverse('update_user_profile'))
    user = request.user
    initial = {
        'first_name':user.first_name,
        'last_name':user.last_name,
        'email':user.email
    }
    user_profile_update = UserProfileUpdate(initial=initial)
    return render(request,'account/user_profile.html',{'form':user_profile_update})
