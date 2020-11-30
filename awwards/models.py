from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Profile(models.Model):
    Profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    prof_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    bio = models.TextField(default="")
    contact_info = models.CharField(max_length=200, blank=True)
    profile_Id = models.IntegerField(default=0)
    all_projects = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)
