from django.db import models

from django.db import models
import random
from django.conf import settings
import uuid
from django.core.exceptions import ValidationError
import string
from django.utils.text import slugify



class AgentName(models.Model):
    '''NAME OF AGENT'''
    name_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

    def __str__(self):
        return f'{self.firstname} - {self.lastname}'
    

class Announced_LGA_Results(models.Model):
    '''announced LGA results'''
    result_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user= models.CharField(max_length=50)
    date_entered=models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.lga_name}'
    

class Announced_PU_Results(models.Model):
    '''announced PU results'''
    result_id = models.IntegerField(primary_key=True)
    # lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    polling_unit_uniqueid = models.IntegerField(null=True)
    entered_by_user= models.CharField(max_length=50)
    date_entered=models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.party_abbreviation} - {self.polling_unit_uniqueid} - {self.party_score}'
    

class Announced_State_Results(models.Model):
    '''announced state results'''
    result_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user= models.CharField(max_length=50)
    # date_entered=models.DateTimeField()
    date_entered=models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.state_name} - {self.party_abbreviation} - {self.party_score}'


class Announced_Ward_Results(models.Model):
    '''announced ward results'''
    result_id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user= models.CharField(max_length=50)
    date_entered=models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.ward_name} - {self.party_abbreviation} - {self.party_score}'


class States(models.Model):
    # state_id = models.IntegerField(primary_key=True)
    state_id = models.IntegerField()
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.state_name}'


class CustomLGAManager(models.Manager):
    def get_queryset(self):
        return super(CustomLGAManager, self).get_queryset().defer('state_id',)

class LGA(models.Model):
    '''LGA'''
    uniqueid = models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    # state = models.ForeignKey('States', on_delete=models.CASCADE, related_name='state_lga')
    # state = models.ForeignKey(States, on_delete=models.CASCADE,related_name='state_lga', null=True)
    lga_description = models.TextField()
    entered_by_user= models.CharField(max_length=50)
    date_entered=models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.lga_name}'


class Party(models.Model):
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.partyid}'
    
    

class Polling_Unit(models.Model):
    
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(null=True, blank=True)
    polling_unit_number = models.CharField(max_length=50,null=True, blank=True)
    polling_unit_name = models.CharField(max_length=50,null=True, blank=True)
    polling_unit_description = models.TextField()
    lat = models.CharField(max_length=255,null=True, blank=True)
    long = models.CharField(max_length=255,null=True, blank=True)
    entered_by_user= models.CharField(max_length=50,null=True, blank=True)
    date_entered=models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50,null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.polling_unit_name} - {self.uniqueid}'
    

class Ward(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField(null=True, blank=True)
    entered_by_user= models.CharField(max_length=50)
    date_entered=models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.ward_name}'
    

class FilterPU(models.Model):
    '''used for temporary filter for PU'''
    lga_id = models.ForeignKey('LGA', on_delete=models.CASCADE)
    ward_id = models.ForeignKey('Ward', on_delete=models.CASCADE)
    pu_id = models.ForeignKey('Polling_Unit', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.lga_id}'