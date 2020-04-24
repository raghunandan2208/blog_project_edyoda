from django.shortcuts import render,redirect
from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from blog.models import Post


# Create your views here.

class UserCreateView(CreateView):
    template_name = "accounts/signup.html"
    form_class = SignUpForm
    success_url = "/accounts/login/"

def profile_page_view(request):
    user = request.user.id
    author_posts = Post.objects.filter(author_id=user).order_by('-date')
    context = {
        'author_posts':author_posts
    }
    return render(request, 'profile/profile.html',context)

@login_required
def profile_page(request,*args, **kwargs):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request, 'profile/profile-update.html',context)
