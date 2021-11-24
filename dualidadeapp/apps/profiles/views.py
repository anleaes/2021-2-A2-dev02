from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm
from .models import Profile

def edit_profile(request, id_user):
    template_name = 'profiles/edit_profile.html'
    context ={}
    profile = get_object_or_404(Profile, user_id=id_user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,  instance=profile)
        if form.is_valid():
            form.save()

    form = ProfileForm(instance=profile)
    context['form'] = form
    return render(request, template_name, context)