from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView, DeleteView
from blog.forms import ContactForm, PostForm
from blog.models import Post, Category
from accounts.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



# Create your views here.


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status = "P").order_by('-date')
    template_name = "blog/stories.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['latest_posts'] = Post.objects.filter(status = "P").order_by('-date')[:4]
        return context


class PostLatestListView(ListView):
    model = Post
    queryset = Post.objects.filter(status = "P").order_by('-date')[:4]
    template_name = "blog/landing.html"
    context_object_name = "latest_posts"


class SearchPostView(ListView):
    model = Post
    queryset = Post.objects.filter(status = "P").order_by('-date')
    template_name = "blog/stories.html"
    context_object_name = "posts"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Post.objects.filter(title__icontains=query)
        return HttpResponse("Product not found")


@login_required
def post_details(request, slug, *args, **kwargs):

    post = get_object_or_404(Post, slug=slug)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    context = {
        'post' : post,
        'is_liked':is_liked,
        'total_likes':post.total_likes(),
        }
    return render(request, 'blog/details.html', context)


@login_required
def like_post(request):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())


def category_buttons(request, id, *args, **kwargs):
    category = Category.objects.all()
    posts = Post.objects.filter(category__id = id).order_by('-date')
    context = {
    'category': category,
    'posts' : posts
    }
    return render(request, 'blog/stories.html', context)


class PostFormView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = "login"
    permission_required = 'blog.add_post'
    model = Post
    template_name = 'blog/post.html'
    form_class = PostForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'author': user}})
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostFormUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url = "login"
    permission_required = 'blog.change_post'
    model = Post
    form_class = PostForm
    template_name = 'blog/post.html'

    def test_func(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        post = Post.objects.get(slug = slug)
        if self.request.user.get_username() == post.author.get_username():
            return True
        else:
            return False

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = User.objects.get(username= self.request.user)
        kwargs.update({'initial':{'author': user}})
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostFormDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('profile')


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = "/blogs"
    template_name = "blog/contactus.html"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# class PostDetailView(LoginRequiredMixin, DetailView):
#     login_url = "login"
#     model = Post
#     template_name = "blog/details.html"


# class PostDetailView(View):
#
#     def get(self, request, id, *args, **kwargs):
#         try:
#             post = Post.objects.get(id = id)
#             context = {
#             'post' : post
#             }
#             return render(request, 'blog/details.html', context)
#         except:
#             return HttpResponse("Invalid ID")




# def post_form_view(request, *args, **kwargs):
#     obj = User.objects.get(username=request.user.username)
#     if request.method == 'GET':
#         form = PostForm(initial={'author':obj})
#         context = {
#         'form' : form
#         }
#         return render(request, 'blog/post.html', context)
#
#     else:
#         form = PostForm(request.POST, request.FILES, initial={'author':obj})
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Thank You")
#         else:
#             return render(request,"blog/post.html", context={'form':form})
#

# class PostFormView(View):
#     def get(self, request, *args, **kwargs):
#         obj = User.objects.get(username=request.user.username)
#         form = PostForm(initial={'author':obj})
#         context = {
#         'form' : form
#         }
#         return render(request, 'blog/post.html', context)
#
#     def post(self, request, *args, **kwargs):
#         form = PostForm(request.POST, request.FILES, initial={'author':obj})
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Thank You")
#         else:
#             return render(request,"blog/post.html", context={'form':form})






# def contactus_view(request, *args, **kwargs):
#     if request.method == 'GET':
#         form = ContactForm()
#         context = {
#         'form' : form
#         }
#         return render(request, "blog/contactus.html", context)
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             return HttpResponse("Thank You")
#         else:
#             return render(request,"blog/contactus.html", context={'form':form})
