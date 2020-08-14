from django.db import models
from django.conf import settings

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone

class Countries(models.Model):
    '''Countries of Owners'''
    countryId = models.AutoField(primary_key=True)
    countryName = models.CharField(max_length=256)
    countryCreatedAt = models.DateTimeField(default=timezone.now)
    countryUpdatedAt = models.DateTimeField(default=timezone.now)

    def update_country(self):
        '''function to update the date of CountryUpdatedAt field'''
        self.countryUpdatedAt = timezone.now()
        self.save()

    def __str__(self):
        '''customers info about Countries'''
        return self.countryName

class States(models.Model):
    '''States of the Countries'''
    stateId = models.AutoField(primary_key=True)
    stateName = models.CharField(max_length=256)
    stateCountryId = models.ForeignKey(Countries, on_delete=models.CASCADE)
    stateCreatedAt = models.DateTimeField(default=timezone.now)
    stateUpdatedAt = models.DateTimeField(default=timezone.now)

    def update_state(self):
        '''function to update the date of stateUpdatedAt field'''
        self.stateUpdatedAt = timezone.now()
        self.save()

    def __str__(self):
        '''customers info about States'''
        return self.stateName

class Cities(models.Model):
    '''Cities of the States'''
    cityId = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=256)
    cityCountryId = models.ForeignKey(Countries, on_delete=models.CASCADE)
    cityStateId = models.ForeignKey(States, on_delete=models.CASCADE)
    cityCreatedAt = models.DateTimeField(default=timezone.now)
    cityUpdatedAt = models.DateTimeField(default=timezone.now)

    def update_city(self):
        '''function to update the date of stateUpdatedAt field'''
        self.cityUpdatedAt = timezone.now()
        self.save()

    def __str__(self):
        '''customers info about States'''
        return self.cityName

class Owners(models.Model):
    '''Pet's Owners'''
    ownerId = models.AutoField(primary_key=True)
    ownerEmail = models.CharField(max_length=256)
    ownerName = models.CharField(max_length=256)     
    ownerAddress = models.CharField(max_length=256)
    ownerPhone = models.CharField(max_length=50)
    ownerCountryId = models.ForeignKey(Countries, on_delete=models.CASCADE)
    ownerStateId = models.ForeignKey(States, on_delete=models.CASCADE)
    ownerCityId = models.ForeignKey(Cities, on_delete=models.CASCADE)
    ownerNeighborhood = models.CharField(max_length=50)
    ownerPetName = models.CharField(max_length=50)
    ownerPetType = models.CharField(max_length=50)
    ownerCreatedAt = models.DateTimeField(default=timezone.now)
    ownerUpdatedAt = models.DateTimeField(default=timezone.now)

    def update_owner(self):
        '''function to update the date of ownerUpdatedAt field'''
        self.ownerUpdatedAt = timezone.now()
        self.save()

    def __str__(self):
        '''customers info about Owners'''
        return self.ownerName