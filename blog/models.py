from django.db import models

#to connect user model with post model
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    #auto_now_add only update this data when the post is created not when it is updated
    date_posted = models.DateTimeField(auto_now_add = True)
    #on_delete basically tells that delete the post if the User itself is deleted
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title