from django.shortcuts import render
from itineraries.models import Itinerary
from django.http import JsonResponse

# Create your views here.
def get_all_user_itinerary(uid):
    sql = """
        SELECT *
        FROM Itineraries
        WHERE uid = %s
    """
    query_results = [r for r in Itinerary.objects.raw(sql, [uid])]
    return JsonResponse(query_results, safe=False)

def insert_new_itinerary():
    # Itinerary.objects.
    pass

def edit_itinerary():
    pass