from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    title = models.CharField(max_length = 200)
    content = models.CharField(max_length = 1000)

    def __str__(self):
        return self.title