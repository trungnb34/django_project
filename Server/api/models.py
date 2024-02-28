from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Colors(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Icons(models.Model):
    code = models.CharField(max_length=10)
    symbol = models.CharField(max_length=50)
    
    def __str__(self):
        return self.symbol

class Categories(models.Model):
    name = models.CharField(max_length=150)
    isEditable = models.BooleanField()
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)
    icon = models.ForeignKey(Icons, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    name = models.CharField(max_length=50)
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(
        verbose_name=_("Creation date"), auto_now_add=True, null=True
    )
    dateTimeDone = models.DateTimeField(auto_now_add=False, null=True)
    def __str__(self):
        return self.name