

#Django 
from django.db import models
#utils models 
from utils.models import GenericModel  
# User model 
from authentication.models import User

class Expense( models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    CATEGORY_OPTIONS =   [
        ('ONLINE_SERVICES', 'ONLINE_SERVICES' ),
        ('TRAVEL', 'TRAVEL' ),
        ('FOOD', 'FOOD' ),
        ('OTHERS', 'OTHERS' ),
    ]
      

    category = models.CharField( 'category',  choices=CATEGORY_OPTIONS,  max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False) 


    class Meta:
        ordering : ['-date']

    def __str__(self):
        return str(self.owner) + 's income'