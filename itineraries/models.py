from django.db import models

def place_json_placeholder():
    google_json_placeholder = dict()
    google_json_placeholder["details"] = "This Place does not have a Google Places JSON attached."
    return google_json_placeholder

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
    place_id_google = models.CharField(max_length=127, null=True, blank=True, default=None)
    place_type = models.CharField(max_length=255, default="general")
    place_lat = models.DecimalField(max_digits=20, decimal_places=15, default=0.0000000000) # 33.866489
    place_lng = models.DecimalField(max_digits=20, decimal_places=15, default=0.0000000000)
    place_google_json = models.JSONField(null=True, default=place_json_placeholder) # stuff from Google Maps API

class PlaceToUser(models.Model):
    class Meta:
        unique_together = ('uid', 'place_id',)
    uid = models.IntegerField()
    place_id = models.IntegerField()
    name = models.CharField(max_length=127, default="Untitled Place")