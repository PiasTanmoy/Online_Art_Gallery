from django.db import models

# Create your models here.

class Exhibition (models.Model):
    exh_id = models.CharField(max_length=100)
    date =models.CharField(max_length=100)
    time =models.CharField(max_length=100)

class Competition (models.Model):
    com_id = models.CharField(max_length=100)
    date =models.CharField(max_length=100)
    time =models.CharField(max_length=100)

