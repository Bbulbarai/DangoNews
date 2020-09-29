
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    name = models.CharField(max_length=1000, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    more = models.TextField(max_length=10000, null=True)
    image = models.ImageField(upload_to='news/images/')
    detailed = RichTextUploadingField()


class Superuser(models.Model):
    lastname = models.CharField(max_length=200, null=True)
    firstname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=8)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class User_model(models.Model):
    lastname = models.CharField(max_length=200, null=True)
    firstname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=8, null=True)
    name = models.CharField(max_length=200, null=True)
    check = models.BooleanField(default=False)

class Login(models.Model):
    name = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=8, null=True)

class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(null=True)