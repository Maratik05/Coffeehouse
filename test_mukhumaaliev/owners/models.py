from django.contrib.auth.models import AbstractUser
# Create your models here.

class Owner(AbstractUser):
    pass
    def __str__(self) -> str:
        return self.first_name