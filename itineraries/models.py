from django.db import models

# Create your models here.
class Itinerary(models.Model):
    tid = models.AutoField(primary_key=True)
    created_by = models.IntegerField()
    archived = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    
    city = models.CharField(max_length=255, default="PLACEHOLDER_CITY")
    state = models.CharField(max_length=255, default="PLACEHOLDER_STATE")
    country = models.CharField(max_length=255, default="PLACEHOLDER_COUNTRY")
    title = models.CharField(max_length=255, default="Untitiled")
    est_budget_up = models.IntegerField(default=10)
    est_budget_down = models.IntegerField(default=0)

    itinerary = models.JSONField()


class ItineraryPermission(models.Model):
    user_itin_pair_id = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    tid = models.IntegerField()