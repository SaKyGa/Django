from django.db import models
from django.contrib.auth.models import User
"""
all objects - SELECT * FROM post ==> Post.objects.all()

one object - SELECT * FROM post WHERE id = 1 ==> Post.objects.get(id=1)

filter objects - SELECT * FROM post WHERE ILIKE ('title') ==> Post.objects.filter(title__contains='title')
"""

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
         return f'{self.name}'
    
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}, {self.content}'
    

