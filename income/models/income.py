

#Django 
from django.db import models
#utils models 
from utils.models import GenericModel  
# User model 
from authentication.models import User

class Income( models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    SOURCE_OPTIONS =   [
        ('SALARY', 'SALARY' ),
        ('BUSINESS', 'BUSINESS' ),
        ('SIDE-HUSTLES', 'SIDE-HUSTLES' ),
        ('OTHERS', 'OTHERS' ),
    ]
      

    source = models.CharField( 'income',  choices=SOURCE_OPTIONS,  max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False) 

    class Meta:
        ordering : ['-date']

    def __str__(self):
        return str(self.owner) + 's income'
    