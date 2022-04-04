from django.db import models
from django.contrib.auth import get_user_model
from .profile import Profile

class Post(models.Model):
    stars = models.CharField(max_length=3)
    content = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    # This must return a string
        return f"{self.profile}  {self.author}  {self.content} {self.stars}"
