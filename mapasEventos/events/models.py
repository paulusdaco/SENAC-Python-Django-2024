from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('music', 'Música'),
        ('show', 'Show'),
        ('museum', 'Museu'),
        ('theater', 'Teatro'),
        # outras categorias...
    ]

    PRICE_CHOICES = [
        ('free', 'Gratuito'),
        ('paid', 'Pago'),
    ]

    LANGUAGE_CHOICES = [
        ('pt', 'Portuguese'),
        ('de', 'German'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('it', 'Italian'),
        ('nl', 'Dutch'),
        ('sv', 'Swedish'),
        # Adicione outros idiomas conforme necessário
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='events/')
    latitude = models.CharField(max_length=10)#FloatField()
    longitude = models.CharField(max_length=10)#FloatField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    #price = models.BooleanField(default=True)
    price = models.CharField(max_length=10, choices=PRICE_CHOICES)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #, default=1
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events_created')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



