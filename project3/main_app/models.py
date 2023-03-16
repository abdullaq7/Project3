from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=700)

    def get_absolute_url(self):
        return reverse("categories", kwargs={"pk": self.id})
    
    def __str__(self):
        return self.name
    
    
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.ManyToManyField(Category, through='UserCategory')

    def __str__(self):
        return self.user.username

class UserCategory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    



