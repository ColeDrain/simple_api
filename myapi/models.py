from django.db import models
import uuid # Generates random uuid

# Create your models here.
class Item(models.Model):

    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    
    timestamp = models.DateTimeField(
        auto_now_add = True, 
        blank = True)

    def __str__(self):
        return f'{self.id}'
    