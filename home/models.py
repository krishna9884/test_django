from django.db import models

# Create your models here.
class info(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=12)
    age=models.CharField(max_length=3)

    def __str__(self):
        return self.name
    
