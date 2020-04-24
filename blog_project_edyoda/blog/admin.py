from django.contrib import admin
from blog.models import Post,Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','status')

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
