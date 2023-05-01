from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.

class Project(models.Model):
    STATUS_CHOICES = (
        ('Won', 'Won'),
        ('Pending', 'Pending'),
        ('Lost', 'Lost'),
        ('Cancelled', 'Cancelled')
    )
    TECHNOLOGY_CHOICES = (
        ('3D', '3D'),
        ('2D', '2D'),
        ('OBN', 'OBN'),
        ('WAZ', 'WAZ')
    )
    
    TYPE_CHOICES = (
        ('MC', 'MC'),
        ('Converted Contract', 'Converted Contract'),
        ('Proprietary', 'Proprietary')
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    technology = models.CharField(max_length=3, choices=TECHNOLOGY_CHOICES) 
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    country = CountryField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.name
        return f'{self.name} - {self.owner}'