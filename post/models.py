from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from tinymce.models import HTMLField
User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    images = models.ImageField(upload_to='media')
    content =  HTMLField()
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)
        
    @property
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur inconnu"
    
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,related_name='comment')
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    body =  models.TextField()
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.post.title
