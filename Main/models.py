from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=1024)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.user.first_name