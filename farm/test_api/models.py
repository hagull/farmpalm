from django.db import models
from django.conf import settings
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
