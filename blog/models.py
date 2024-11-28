from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default='Admin')  # Modify if you integrate with users
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
