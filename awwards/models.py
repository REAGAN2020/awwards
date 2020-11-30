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

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    def update_bio(self, bio):
        self.bio = bio
        self.save()
    @classmethod
    def get_profile_data(cls):
        return Profile.objects.all()

    class Meta:
        db_table = 'profiles'

class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    link = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to='project_images', blank=True)
    user_project_id = models.IntegerField(default=0)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    creativity = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    @classmethod
    def fetch_all_images(cls):
        all_images = Project.objects.all()
        return all_images

    @classmethod
    def get_single_project(cls, project):
        project = cls.objects.get(id=project)
        return project
    @classmethod
    def search_project_by_title(cls, search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project
    class Meta:
        db_table = 'projects'
        ordering = ['-id']
    
class Comment(models.Model):
    comment = models.CharField(max_length=80, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)   




