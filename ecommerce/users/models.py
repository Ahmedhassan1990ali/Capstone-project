from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password,**kwargs):
        if not username:
            raise ValueError("Name must be set")
        if not email:
            raise ValueError("email must be provided")
        if not password:
            raise ValueError("Password must be provided")
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user    
    
    def create_superuser(self,username,email,password,**kwargs):
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser",True)
        if kwargs.get("is_staff")is not True:
            raise ValueError("Superuser must have is_staff=True")
        if kwargs.get("is_superuser")is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(username,email,password,**kwargs)
        
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username