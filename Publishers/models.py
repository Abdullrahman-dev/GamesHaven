from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    logo = models.ImageField(upload_to="images/",default="images/default.png")

    def __str__(self):
        return self.name