from django.db import models

# Create your models here.
class Itinerary(models.Model):
    tid = models.AutoField(primary_key=True)
    created_by = models.IntegerField()
    archived = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    forked_from = models.IntegerField(null=True, blank=True, default=None)
    last_modified_at = models.DateTimeField(auto_now=True)
    
    city = models.CharField(max_length=255, default="PLACEHOLDER_CITY")
    state = models.CharField(max_length=255, default="PLACEHOLDER_STATE")
    country = models.CharField(max_length=255, default="PLACEHOLDER_COUNTRY")
    title = models.CharField(max_length=255, default="Untitiled")
    description = models.CharField(max_length=1024, default="This itinerary does not have a description yet...")
    est_budget_up = models.IntegerField(default=10)
    est_budget_down = models.IntegerField(default=0)

    itinerary = models.JSONField()

class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_type = models.CharField(max_length=255, default="general")
    place_x_coordinate = models.DecimalField(decimal_places=5, max_digits=10, default=0.0)
    place_y_coordinate = models.DecimalField(decimal_places=5, max_digits=10, default=0.0)
    place_google_link = models.CharField(max_length=512, default="https://goo.gl/maps/6N5kYyXZWXFNiivE7")
    place_json_info = models.JSONField() # stuff from Google Maps API

class PlaceToUser(models.Model):
    class Meta():
        pass
    uid = models.IntegerField()
    place_id = models.IntegerField()