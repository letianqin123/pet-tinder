from django.db import models
from  django.contrib.auth import get_user_model
User=get_user_model()
from pet.models import Pet
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Likes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(10)])
    created_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return  self.pet.name
    