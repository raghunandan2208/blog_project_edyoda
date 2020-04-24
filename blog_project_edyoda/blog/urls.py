from django.urls import path,re_path
# from blog.views import index
from blog.views import post_details, like_post
from blog.views import category_buttons
# from blog.views import post_form_view
# from blog.views import contactus_view
from blog.views import PostListView, PostFormView, ContactFormView, PostFormUpdateView, PostLatestListView, PostFormDeleteView, SearchPostView


urlpatterns = [
    path('', PostLatestListView.as_view(),name='landing'),
    path('index', PostListView.as_view(), name='index'),
    path('filter/<int:id>', category_buttons, name='category_buttons'),
    path('search', SearchPostView.as_view(), name='search'),
    # path('posts', post_form_view, name='posts'),
    path('posts', PostFormView.as_view(), name='posts'),
    path('update/<slug:slug>', PostFormUpdateView.as_view(), name='update-view'),
    path('delete/<slug:slug>', PostFormDeleteView.as_view(), name='delete-view'),
    path('contacts', ContactFormView.as_view(), name='contacts'),
    path('like',like_post,name='like_post'),
    # path('dashboard',dashboard,name='dashboard'),
    path('<str:slug>', post_details, name='post-detail'),
    # path('<slug:slug>', PostDetailView.as_view(), name='post-detail'),

]
