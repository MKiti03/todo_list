from operator import truediv
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserManager(BaseUserManager):
    
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError(_("You should the user email address"))
        
        if not username:
            raise ValueError(_("You should the user Username"))
        
        if not password:
            raise ValueError(_("You should the user password"))
        
        email = self.normalize_email(email)
        
        user = self.model(username = username, email =email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Super User must have is_superuser = True"))
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Super User must have is_staff = True"))
        
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Super User must have is_active = True"))
        
        
        return self.create_user(email, username, password, **extra_fields)
    
class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=False, unique=True)
    email = models.EmailField(max_length=150, null=True, blank=False, unique=True)
    
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True),
    
    address = models.CharField(max_length=255, null=True, blank=True)
    date_joined = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    last_update = models.DateTimeField(blank=True, null=True, auto_now=True)
    
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = "username"
    
    objects = UserManager()
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]
        
    def __str__(self):
        return self.username
        
        