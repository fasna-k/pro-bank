from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(default=False)
    

    def __str__(self):
        return self.name