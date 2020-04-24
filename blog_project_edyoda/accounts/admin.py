from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
from accounts.models import Profile
# Register your models here.


admin.site.register(Profile)

admin.site.register(User, UserAdmin)
