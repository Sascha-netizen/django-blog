from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=300)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f" {self.title} "
    

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request form {self.name}"