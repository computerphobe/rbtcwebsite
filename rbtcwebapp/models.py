from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.db.models import F
from model_utils import FieldTracker
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, blank=True)
    enroll_no = models.PositiveBigIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Category(models.Model):
    name = models.CharField(max_length=100)

class Component(models.Model):
    CATEGORY_CHOICES = [
        ('Drone', 'Drone'),
        ('Battery', 'Battery & Power'),
        ('Sensors', 'Sensors'),
        ('Actuators', 'Actuators'),
        ('IOT', 'IOT'),
        ('Other', 'Other'),
        ('Miscellaneous', 'Miscellaneous'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='Other'  # Default category for existing rows
    )
    image = models.ImageField(upload_to='components', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        """Return image URL or default image if none exists"""
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
class IssuedComponent(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Returned', 'Returned'),
    ]
    
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name="issues")
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
    )
    issue_date = models.DateField(default=now)
    return_date = models.DateField(null=True, blank=True)
    purpose = models.TextField(blank=True)

    
    # Add tracker to monitor status changes
    tracker = FieldTracker(fields=['status'])
    
    def clean(self):
        if self.quantity <= 0:
            raise ValidationError({'quantity': 'Quantity must be greater than 0'})
        
        if self.status == 'Approved' and self.component.quantity < self.quantity:
            raise ValidationError({
                'quantity': f'Insufficient stock. Available: {self.component.quantity}, Requested: {self.quantity}'
            })
    
    def __str__(self):
        return f"{self.component.name} - {self.quantity} units ({self.status})"



