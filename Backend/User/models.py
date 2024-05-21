from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone

class NewUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20,null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, null= True)
    last_name = models.CharField(max_length=30,null=True)
    dob = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='', null=True, blank=True)
    age= models.IntegerField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    
    objects = UserManager()

    def __str__(self):
        return self.email

