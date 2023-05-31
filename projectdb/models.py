from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone
# Create your models here.

class Permit(models.Model):
    agencies = (        
        ("ANP", "ANP"),
        ("IBAMA", "IBAMA"),
        ("DNPM", "DNPM"),
        ("MMA", "MMA"),
        ("MME", "MME"),
        ("ANH", "ANH"),
        ("ANLA", "ANLA"),
        ("SNE_ARG","SNE_ARG"),
        ("SNE_BOL", "SNE_BOL"),
        ("ANCAP","ANCAP"),
        ("CNH", "CNH"),
        ("Staatsolie","Staatsolie"),
        ("MEEI", "Ministry of Energy and Energy Industries (MEEI)"),
        ("MEB","Ministry of Energy and Business (MEB)"),
        ("MSET","Jamaica (MSET)")
        )
    
    STATUS_CHOICES = (
        ('In Application', 'In Application'),
        ('Not Started', 'Not Started'),
        ('Denied', 'Denied'),
        ('Cancelled', 'Cancelled'),
        ('Valid', 'Valid')
    )
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='permits')
    permit_name = models.CharField(max_length=100)
    country = CountryField()
    regulatory_agency = models.CharField(max_length=10, choices=agencies, default='None')
    permit_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    application_date = models.DateField()
    granted_on = models.DateField(default=None, blank=True, null=True)
    validity_period = models.IntegerField(default=None, blank=True, null=True)
    expiry_date = models.DateField(editable=False)

    def save(self, *args, **kwargs):
        if self.granted_date and self.validity_period:
            self.expiry_date = self.granted_date + timezone.timedelta(days=self.granted_date * 365)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.permit_name


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
        ('WAZ', 'WAZ'),
        ('2D Repro', '2D Repro'),
        ('3D Repro', '3D Repro'),
        ('OBN Repro', 'OBN Repro')
    )
    
    TYPE_CHOICES = (
        ('MC', 'MC'),
        ('Converted Contract', 'Converted Contract'),
        ('Proprietary', 'Proprietary')
    )
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    technology = models.CharField(max_length=10, choices=TECHNOLOGY_CHOICES) 
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='MC')
    country = CountryField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    start_date = models.DateField(default=None, blank=True, null=True)
    end_date = models.DateField(default=None, blank=True, null=True)
    permit = models.ForeignKey(Permit, on_delete=models.CASCADE, related_name='projects',default=None, blank=True, null=True) 

    def __str__(self):
        # return self.name
        return f'{self.name} - {self.owner}'