from django.db import models

# Create your models here.
class Flavour(models.Model):    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    launched_on = models.DateField()
    vegan_available = models.BooleanField()
    location = models.TextField()
    limited_edition = models.BooleanField()
    customers = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.name
