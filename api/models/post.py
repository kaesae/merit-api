from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=40)
    stars = models.CharField(max_length=3)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    # This must return a string
        return f"{self.title}  {self.author}  {self.content} {self.stars}"


# blog ---> profile / comment --> post

# Create Comment Model

# class Post(models.Model):
#     content = models.CharField(max_length=250)
#     stars = models.CharField(max_length=3)
#     profile = models.ForeignKey(
#         Profile,
#         on_delete=models.CASCADE,
#         null=True
#     )
#     author = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         # This must return a string
#         return f"Comments"