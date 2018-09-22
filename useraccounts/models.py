import time
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date
from django.db import models
# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=256, default = " ",null=True, blank = True)
    cell = models.CharField(max_length=256, default = " ",null=True, blank = True)
    phone       =models.CharField(max_length=14, default = 0,null=True, blank = True)
    dob         = models.DateField(max_length=14, default = "",null=True, blank = True)
    address     = models.CharField(max_length=14, null=True, blank = True)
    
    def __str__(self):
        return self.user.username

class Trader(models.Model):
    occupation = models.CharField(max_length=256, null=True, blank = True)
    phone       = models.CharField(max_length=14, null=True, blank = True)
    fname       = models.CharField(max_length=14, null=True, blank = True)
    lname       = models.CharField(max_length=14, null=True, blank = True)
    dob         = models.DateField(max_length=14, null=True, blank = True)
    city        = models.CharField(max_length=14, null=True, blank = True)
    address     = models.CharField(max_length=14, null=True, blank = True)
    trade_address   = models.CharField(max_length=50, null=True, blank = True)
    products    = models.CharField(max_length=14, null=True, blank = True)
    business_date    =  models.DateField(max_length=14, null=True, blank = True)
    business_worth    = models.IntegerField(null=True, blank = True)
    have_kids    = models.BooleanField( blank = True)
    num_kids     = models.IntegerField(null=True, blank = True)
    with_spouse    = models.BooleanField( blank = True)
    why_no_spouse    = models.CharField(max_length=20, null=True, blank = True)
    business_needs    = models.CharField(max_length=14, null=True, blank = True)
    income     = models.IntegerField(null=True, blank = True)
    supplier    = models.CharField(max_length=20, null=True, blank = True)
    change_business    = models.BooleanField( blank = True)
    fund_needed     = models.IntegerField(null=True, blank = True)
    do_you_save     = models.BooleanField( blank = True)
    cell_leader     = models.ForeignKey(User, on_delete = models.CASCADE)
    cell_name        = models.CharField(max_length=14, null=True, blank = True)
    added   = models.DateField( auto_now=True)
    slug        = models.SlugField(max_length=150, unique=True ,db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fname) + slugify(self.lname) + slugify(self.phone)
        super(Trader, self).save(*args, **kwargs)

    def __str__(self):
        return self.fname + self.lname

class Funds(models.Model):
    amount  = models.IntegerField(null=True, blank = True)
    trader     = models.ForeignKey(Trader, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Fund'
