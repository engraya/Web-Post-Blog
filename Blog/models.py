from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    profession = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    country = CountryField(blank_label='Select Country')
   

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    