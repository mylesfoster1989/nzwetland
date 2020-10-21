from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Site(models.Model):
    sitename = models.CharField(max_length=25, null=False, blank=False)
    area = models.FloatField(validators=[MaxValueValidator(9999999999), MinValueValidator(100)], null=False, blank=False)
    altitude = models.FloatField(validators=[MaxValueValidator(99999), MinValueValidator(0)], null=False, blank=False)
    types = (
        ('Strict Nature Reserve', 'Strict Nature Reserve'),
        ('National Park', 'National Park'),
        ('Wildlife Reserve', 'Wildlife Reserve'),
        ('State Reserve', 'State Reserve'),
        ('Hunting Reserve', 'Hunting Reserve'),

    )
    sitetype = models.CharField( choices=types,max_length=30, null=False, blank=False)
    statustype = (
        ('Normal', 'Normal'),
        ('Threatend', 'Threatend'),
    )
    status = models.CharField(choices=statustype,max_length=10, null=False, blank=False)

class Habitat(models.Model):
    description = models.CharField(max_length=40, null=False, blank=False)
    habitattype = models.CharField(max_length=30, null=False, blank=False)


class Landuse(models.Model):
    description = models.CharField(max_length=40, null=False, blank=False)
    landusetype = models.CharField(max_length=30, null=False, blank=False)

class Sponsor(models.Model):
    sponsorname = models.CharField(max_length=25, null=False, blank=False)
    streetaddress = models.CharField(max_length=50, null=False, blank=False)
    suburb = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=25, null=False, blank=False)
    phonenumber = models.CharField(max_length=16, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)




class Animal(models.Model):
    commonname = models.CharField(max_length=25, null=False, blank=False)
    genusname = models.CharField(max_length=25, null=False, blank=False)
    speciesname= models.CharField(max_length=25, null=False, blank=False)

    animaltype = (
        ('Bird', 'Bird'),
        ('Mammal', 'Mammal'),
        ('Reptile', 'Reptile'),
        ('Fish', 'Fish'),
    )
    type = models.CharField(choices=animaltype,max_length=10, null=False, blank=False)

class SiteHabitat(models.Model):
    sitehabitatname = models.CharField(max_length=25, null=False, blank=False)
    area = models.FloatField(validators=[MaxValueValidator(9999999999), MinValueValidator(100)], null=False,
                                 blank=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=False,
                               blank=False)
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE, null=False,
                             blank=False)

class Survey(models.Model):
    surveyname = models.CharField(max_length=25, null=False, blank=False)
    budget = models.FloatField(validators=[MaxValueValidator(50000), MinValueValidator(500)], null=False,
                               blank=False)
    startdate = models.DateField(null=False, blank=False)
    enddate = models.DateField(null=False, blank=False)
    statustype1 = (
        ('Ratified', 'Ratified'),
        ('Unratified', 'Unratified'),
    )
    status = models.CharField(choices=statustype1,max_length=10, null=False, blank=False)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=False,
                               blank=False)

class Observation(models.Model):
    observationstatus = (
        ('Confirmed', 'Confirmed'),
        ('Unconfirmed', 'Unconfirmed'),

    )
    status = models.CharField(choices=observationstatus,max_length=11, null=False, blank=False)
    observationnumber = models.FloatField(validators=[MaxValueValidator(300), MinValueValidator(1)], null=False,
                             blank=False)
    observationdate = models.DateField(null=False, blank=False)
    sitehabitat = models.ForeignKey(SiteHabitat, on_delete=models.CASCADE,  null=False,
                                     blank=False)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=False,
                                    blank=False)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=False,
                               blank=False)

class Sitehabitatlanduse(models.Model):
    impacts = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),

    )
    impact = models.CharField(max_length=6,choices=impacts, null=False, blank=False)

    sitehabitat = models.ForeignKey(SiteHabitat, on_delete=models.CASCADE, null=False,
                                blank=False)
    landuse = models.ForeignKey(Landuse, on_delete=models.CASCADE, null=False,
                                    blank=False)









