from django.contrib.auth.models import User
# Create your models here.

class Owner(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __str__(self) -> str:
        return self.username
    
