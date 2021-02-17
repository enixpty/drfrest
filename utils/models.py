""" Django models utilities """

#django
from django.db import models

class GenericModel(models.Model):
    """
    GenericModel Base Model

    GenericModel acts as an abstract base class from which every 
    other model in the project will inherit. this class provides
    every table with the following attributes:
        + created (DateTime) : Store the datetime the object was created.
        + modified (DateTime) : Store the last datetime the object was modified
    """
    created = models.DateField( ("created at"),  
                                auto_now_add=True,
                                help_text='Date time on which the object was created'
    )

    modified = models.DateField( ("modified at"), 
                                    auto_now=True, 
                                    help_text='Date time on which the object was last modified' 
    )

    class Meta:
        
        """ Meta option """

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']