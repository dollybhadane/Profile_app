from django.shortcuts import render, get_object_or_404
from .models import Profile

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})

def show_map(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'profiles/show_map.html', {'profile': profile})