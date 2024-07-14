from django.db import models

# Create your models here.



class MyProjects(models.Model):
    title = models.CharField(max_length = 64)
    image = models.ImageField(upload_to="project_images")
    github_link = models.CharField(max_length = 512)
    live_link = models.CharField(max_length = 512)
    def __str__(self):
        return self.title
    

class MyFrontEndSKills(models.Model):
    name = models.CharField(max_length = 64)
    icon = models.ImageField(upload_to="skills_icons")
    def __str__(self):
        return self.name

class MyBackEndSKills(models.Model):
    name = models.CharField(max_length = 64)
    icon = models.ImageField(upload_to="skills_icons")
    def __str__(self):
        return self.name

