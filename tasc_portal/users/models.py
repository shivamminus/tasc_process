from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models

class TeamUser(AbstractUser):
    is_reviewer = models.BooleanField(default=False)
    team_name = models.CharField(max_length=255, blank=True, null=True)