from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=30, unique=True, blank=True, null=True)
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
