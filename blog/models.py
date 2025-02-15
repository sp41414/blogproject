from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
            (DRAFT, 'Draft'),
            (PUBLISHED, 'Published'),
            ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager() # there was some kinda error and it shut up because of this, so keep it?
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
        return self.title
