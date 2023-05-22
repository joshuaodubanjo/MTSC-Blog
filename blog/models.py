from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

STATUS = (
    ("Draft", "Draft"),
    ("Published", "Published"),
)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    content = models.TextField()
    img = models.ImageField(upload_to='post_img')
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    published = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS, default='draft')
    tag = models.ManyToManyField('Tag')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=255)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title