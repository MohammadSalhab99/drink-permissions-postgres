from django.db import models
from django.contrib.auth import get_user_model

class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    customer =models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name