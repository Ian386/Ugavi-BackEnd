from django.db import models
from django.contrib.gis.db import models as gis_models


# Create your models here.
class Location(models.Model):
    LABEL_CHOICES = [
        ('farms', 'Farm'),
        ('processing-facilities', 'Processing Facility'),
        ('distribution-centers', 'Distribution Center'),
        ('warehouses', 'Warehouse'),
        ('restaurants', 'Restaurant'),
        ('supermarkets', 'Supermarket')
    ]
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100, choices=LABEL_CHOICES)
    location = gis_models.PointField(srid=4326)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField()


    def _str_(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Locations'


class Farmer(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length = 20)


    def _str_(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Farmers'


class Farm(models.Model):
    REGION_CHOICES = [
        ('central', 'Central'),
        ('coast', 'Coast'),
        ('eastern', 'Eastern'),
        ('nairobi', 'Nairobi'),
        ('north_eastern', 'North Eastern'),
        ('nyanza', 'Nyanza'),
        ('rift_valley', 'Rift Valley'),
        ('western', 'Western')
    ]
    name = models.CharField(max_length=100)
    farm_area =gis_models.PolygonField(srid=4326)
    description = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=100, choices=REGION_CHOICES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='farms')
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='farms')
    
    

    def str(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Farms'


class Crop(models.Model):
    name = models.CharField(max_length=100)
    crop_type= models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='crops')

    def _str_(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Crops'
