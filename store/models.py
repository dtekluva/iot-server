import time
from django.template.defaultfilters import slugify
from datetime import date
from django.db import models
from useraccounts.models import UserAccount, User
from snippets.resize import shrink
# Create your models here.




class Device(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=150, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Device, self).save(*args, **kwargs)
 
    class Meta:
        ordering = ('name', )
 
    def __str__(self):
        return self.name

class Sensor_Post(models.Model):
    device = models.ForeignKey(Device, related_name='products', on_delete=models.CASCADE)
    co_val = models.IntegerField( default = 0)
    ch4_val = models.IntegerField( default = 0)
    aq_val = models.IntegerField( default = 0)
    h_val = models.IntegerField( default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    sensor_time = models.DateTimeField( null=True, blank = True)
    image = models.ImageField(upload_to='store/product_imgs', blank=True)
