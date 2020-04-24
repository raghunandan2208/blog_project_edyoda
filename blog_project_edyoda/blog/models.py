from django.db import models
from django.utils import timezone
from accounts.models import User
from tinymce import models as tinymce_models
from django.utils.text import slugify
from django.urls import reverse
import readtime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    statuses = [
        ("D", "Draft"),
        ("P","Publish"),
    ]
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=100, unique=True)
    content = tinymce_models.HTMLField()
    likes  = models.ManyToManyField(User,related_name='likes',blank = True)
    status = models.CharField(max_length=1, choices = statuses)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/post',default='blog/post/default-post.jpg', blank = True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug':self.slug})

    def total_likes(self):
        return self.likes.count()

    def get_readtime(self):
        result = readtime.of_text(self.content)
        return result.text
