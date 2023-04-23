from django.shortcuts import render
from itineraries.models import Itinerary, Place, PlaceToUser
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from rest_framework import status
import json
import jwt

SECRET = 'django-insecure-a(o^i#n&lao7enyg-b1(2c73qxvmt7p=#azi=os3i@ub9$b9)$'

@csrf_exempt
def get_all_user_itin(request):

    # if method is not GET, return 405.
    if (request.method != "POST"): return JsonResponse({'Error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    required_fields = ["jwt", "uid"]
    parse_request_results = parse_and_verify_request(request, required_fields)
    if not parse_request_results[0]: return parse_request_results[1]

    # get all itineraries created by the user.
    rbody = parse_request_results[1]
    res = Itinerary.objects.filter(created_by=rbody["uid"])
    query_res_list = [i.__dict__ for i in list(res)]
    for i in query_res_list: i['_state'] = "" # don't know what this is but its messing up the serialization stuff

    return JsonResponse(query_res_list, safe=False)


@csrf_exempt
def insert_new_itin(request):

    if (request.method != "POST"):  return JsonResponse({'Error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    required_fields = ["uid", "jwt", "itinerary"]
    parse_request_results = parse_and_verify_request(request, required_fields)
    if not parse_request_results[0]: return parse_request_results[1]

    rbody = parse_request_results[1]
    newItin = Itinerary(
        created_by = rbody["uid"],
        archived = False if not "archived" in rbody else rbody["archived"],
        private = False if not "private" in rbody else rbody["private"],
        city = "CITY_UNDEFINED" if not "city" in rbody else rbody["city"],
        state = "STATE_UNDEFINED" if not "state" in rbody else rbody["state"],
        country = "COUNTRY_UNDEFINED" if not "country" in rbody else rbody["country"],
        title = "Untitled Itinerary" if not "title" in rbody else rbody["title"],
        est_budget_up = 0 if not "est_budget_up" in rbody else rbody["est_budget_up"],
        est_budget_down = 0 if not "est_budget_down" in rbody else rbody["est_budget_down"],
        description = "This itinerary does not have a description yet." if not "description" in rbody else rbody["description"],
        itinerary = rbody["itinerary"],
        )
    newItin.save()
    return JsonResponse({'Success': 'Itinerary saved to server successfully.'}, status=status.HTTP_200_OK)


@csrf_exempt
def edit_itin(request):
    if (request.method == "POST"):
        required_fields = [
            "uid", 
            "jwt", 
            "tid", 
            "archived", 
            "private", 
            "city", 
            "state", 
            "country", 
            "title", 
            "est_budget_up", 
            "est_budget_down", 
            "itinerary",
            "description",
        ]
        parse_request_results = parse_and_verify_request(request, required_fields)
        if not parse_request_results[0]: return parse_request_results[1]
        rbody = parse_request_results[1]
        try:
            query_res = Itinerary.objects.get(tid=rbody["tid"])
        except Itinerary.DoesNotExist:
            return JsonResponse({'Error': 'Itinerary not found.'}, status=status.HTTP_404_NOT_FOUND)
        try:
            query_res.archived = rbody["archived"]
            query_res.private = rbody["private"]
            query_res.city = rbody["city"]
            query_res.state = rbody["state"]
            query_res.country = rbody["country"]
            query_res.title = rbody["title"]
            query_res.est_budget_up = rbody["est_budget_up"]
            query_res.est_budget_down = rbody["est_budget_down"]
            query_res.itinerary = rbody["itinerary"]
            query_res.description = rbody["description"]
            query_res.last_modified_at = datetime.now()
            query_res.save()
        except:
            return JsonResponse({'Error': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse({"Success": "Changes saved to server successfully."}, safe=False)
    

    elif (request.method == "DELETE"):
        required_fields = ["tid", "jwt", "uid"]
        parse_request_results = parse_and_verify_request(request, required_fields)
        if not parse_request_results[0]: return parse_request_results[1]
        rbody = parse_request_results[1]
        try:
            tid = rbody["tid"]
            Itinerary.objects.get(tid=tid).delete()
            return JsonResponse({'Success': 'Itinerary deleted.'})
        except:
            return JsonResponse({'Error': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    else:
        return JsonResponse({'Error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def get_public_itin(request):
    # if method is not GET, return 405.
    if (request.method != "GET"): return JsonResponse({'Error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    query_res = Itinerary.objects.filter(private=0, archived=0)
    query_res_list = [i.__dict__ for i in list(query_res)]
    for i in query_res_list: i['_state'] = "" # don't know what this is but its messing up the serialization stuff
    return JsonResponse(query_res_list, safe=False)

@csrf_exempt
def get_itin(request):
    # if method is not GET, return 405.
    if (request.method != "POST"):
        return JsonResponse({'Error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    required_fields = ["uid", "jwt", "tid"]
    parse_request_results = parse_and_verify_request(request, required_fields, must_verify=False)
    if not parse_request_results[0]: return parse_request_results[1]

    rbody = parse_request_results[1]
    try:
        query_res = Itinerary.objects.get(tid=rbody["tid"])
    except Itinerary.DoesNotExist:
        # if given itinerary does not exist, return 404.
        return JsonResponse({'Error': 'Itinerary does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    query_res = query_res.__dict__
    query_res['_state'] = ""
    if (query_res["private"]):
        if not (verify_jwt(rbody["jwt"], query_res["created_by"])):
            return JsonResponse({'Error': 'Authentication failed.'}, status=status.HTTP_401_UNAUTHORIZED)
    return JsonResponse(query_res, safe=False)


@csrf_exempt
def insert_place(request):
    if (request.method != "POST"): return JsonResponse({'Error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    parse_request_results = parse_and_verify_request(request, required_fields=[])
    if not parse_request_results[0]: return parse_request_results[1]

    try:
        rbody = parse_request_results[1]
        new_place = Place(
            place_id_google = None if not "place_id_google" in rbody else rbody["place_id_google"],
            place_type = "General" if not "place_type" in rbody else rbody["place_type"],
            place_lat = 0.0000000 if not "place_lat" in rbody else rbody["place_lat"],
            place_lng = 0.0000000 if not "place_lng" in rbody else rbody["place_lng"],
            place_google_json = {"details": "Google Places JSON not provided."} if not "place_google_json" in rbody else rbody["place_google_json"],
        )
        new_place.save()
    except Exception as e:
        print(e)
        return JsonResponse({'False': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JsonResponse({'Success': 'Place saved to server successfully.'}, status=status.HTTP_200_OK)


@csrf_exempt
def user_places(request):
    if request.method == "POST":
        parse_request_results = parse_and_verify_request(request, required_fields=["place_id"])
        if not parse_request_results[0]: return parse_request_results[1]
        rbody = parse_request_results[1]

        try:
            query_res = Place.objects.get(place_id=rbody["place_id"])
        except Place.DoesNotExist:
            # if given itinerary does not exist, return 404.
            return JsonResponse({'Error': 'Itinerary does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        query_res = query_res.__dict__
        query_res['_state'] = ""
        return JsonResponse(query_res, safe=False)

    elif request.method == "POST":
        required_fields = ["jwt", "uid", "place_id", "name"]
        parse_request_results = parse_and_verify_request(request, required_fields)
        if not parse_request_results[0]: return parse_request_results[1]

        try:
            rbody = parse_request_results[1]
            new_entry = PlaceToUser(
                uid=rbody["uid"],
                place_id=rbody["place_id"],
                name=rbody["name"]
            )
            new_entry.save()
        except:
            return JsonResponse({'False': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse({'Success': 'Place saved.'}, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        required_fields = ["place_id", "jwt", "uid"]
        parse_request_results = parse_and_verify_request(request, required_fields)
        if not parse_request_results[0]: return parse_request_results[1]
        rbody = parse_request_results[1]
        try:
            PlaceToUser.objects.get(uid=rbody["uid"], place_id=rbody["place_id"]).delete()
            return JsonResponse({'Success': 'Place deleted.'})
        except:
            return JsonResponse({'Error': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    else:
        return JsonResponse({'Error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def get_my_places(request):
    if request.method != "GET": return JsonResponse({'Error': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    parse_request_results = parse_and_verify_request(request, required_fields=["uid"])
    if not parse_request_results[0]: return parse_request_results[1]
    try:
        rbody = parse_request_results[1]
        res = PlaceToUser.objects.filter(uid=rbody["uid"])
        query_res_list = [i.__dict__ for i in list(res)]
        for i in query_res_list: i['_state'] = ""
        return JsonResponse(query_res_list, safe=False)
    except:
        return JsonResponse({'Error': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def parse_and_verify_request(request, required_fields, must_verify=True):
    parse_request_results = parse_request(request, required_fields)
    # if the body does not contain required fields, return 400 error code.
    if not parse_request_results[0]:
        return False, JsonResponse({'Error': 'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)
    rbody = parse_request_results[1]
    # if the JWT is invalid, return 401 error code.
    if "jwt" in required_fields and must_verify:
        if not verify_jwt(rbody["jwt"], rbody["uid"]):
            return False, JsonResponse({'Error': 'Authentication failed, please try logging in again.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    return True, rbody

def verify_jwt(token, uid):
    try:
        header_data = jwt.get_unverified_header(token)
        payload = jwt.decode(
            token, 
            key=SECRET,
            algorithms=[header_data['alg'], ]
        )
        if str(payload["user_id"]) != str(uid):
            raise(Exception)
        return True
    except Exception as e:
        print(e)
    return False

def parse_request(request, required_fields=[]):
    if request.body:
        body_unicode = request.body.decode('utf-8')
        rbody = json.loads(body_unicode)
        for field in required_fields:
            if field not in rbody:
                return (False, [])
        return (True, rbody)
    return (False, [])