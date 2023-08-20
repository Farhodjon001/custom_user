from django.db import models
from  django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    CHOICES=(
        (1,'admin'),
        (2,'user')
    )
    roles=models.PositiveIntegerField(default=1,choices=CHOICES)




