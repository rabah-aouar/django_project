from distutils.command.upload import upload
from email.mime import image
from email.policy import default
import os
from pyexpat import model
import site
from statistics import mode
from tkinter import CASCADE
from tkinter.tix import Balloon
from turtle import title
from unicodedata import category
from uuid import uuid4
from django.db import models
from users.models import User

# Create your models here.



class Conference(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    description=models.TextField(max_length=3000,blank=False,null=False)
    categories=models.CharField(max_length=500,blank=False,null=False)
    name_of_host=models.CharField(max_length=200,blank=False,null=False)
    start_date=models.DateTimeField(max_length=100,blank=False,null=False)
    end_date=models.DateTimeField(max_length=100,blank=False,null=False)
    location=models.CharField(max_length=200,blank=False,null=False)
    site=models.CharField(max_length=200,blank=False,null=False)
    logo=models.ImageField(upload_to='logos',blank=True,default='hello')
    status=models.CharField(max_length=15,default='waiting')
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='conference_creator',editable=False)
    reviewers=models.ManyToManyField(User,related_name='conference_reviewers')
    applied_personnes=models.ManyToManyField(User,related_name='conference_applied_personnes')
    accepted_personnes=models.ManyToManyField(User,related_name='conference_accepted_personnes')

    
    def __str__(self):
        return(self.title)
