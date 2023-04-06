from django.db import models
from jsonfield import JSONField

# Create your models here.
class Itinerary(models.Model):
    tid = models.IntegerField()
    uid = models.IntegerField()
    archived = models.BooleanField()
    private = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    content = JSONField()