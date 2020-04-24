from django.urls import path, include
from accounts.views import UserCreateView, profile_page, profile_page_view
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView



urlpatterns = [
    path('login/', LoginView.as_view(template_name = "accounts/login.html"), name='login'),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('', include('django.contrib.auth.urls')),
    path('password-reset/', PasswordResetView.as_view(template_name="accounts/password_reset_form.html", email_template_name="accounts/password_reset_email.html"), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="accounts/password_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name='password_reset_complete'),
    path('password-change/', PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('profile/', profile_page_view, name='profile'),
    path('profile-update/', profile_page, name='profile-update'),

]
