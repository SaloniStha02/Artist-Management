from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import UserManager
from django.utils import timezone

class NewUser(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    username = models.CharField(max_length=20,null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    dob = models.DateField(null=True)
    bio= models.TextField(null=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='', null=True, blank=True)
    is_artist = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
   
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def is_administrator(self):
        return self.is_staff and self.is_superuser

    def is_artist_user(self):
        return self.is_artist

    def is_regular_user(self):
        return not self.is_staff and not self.is_superuser and not self.is_artist
    
    def delete(self,hard_delete=False):
        if hard_delete:
            super().delete()
        else:
            self.is_deleted=True
            self.save()
            
    def restore(self):
        self.is_deleted=False
        self.save()

