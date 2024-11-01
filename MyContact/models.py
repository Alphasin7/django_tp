from django.db import models

# Create your models here.
class contact (models.Model):
    firstname =models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    email=models.EmailField(default="")
    message=models.TextField(default="")
    def __str__(self):
        return f"{self.firstname}: " f"{self.lastname}: "f"{self.email}: "
    


    
