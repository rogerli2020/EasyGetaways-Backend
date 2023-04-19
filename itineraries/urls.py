from django.urls import path
from . import views

urlpatterns = [
    path('get_all_user_itin/', views.get_all_user_itin, name='get_all_user_itin'),
    path('insert_new_itin/', views.insert_new_itin, name='insert_new_itinerary'),
    path('edit_itin/', views.edit_itin, name='edit_itinerary'),
    path('get_public_itin/', views.get_public_itin, name='get_public_itin'),
    path('get_itin/', views.get_itin, name='get_itin'),
    path('insert_place/', views.insert_place, name='insert_place'),
    path('get_my_places/', views.get_my_places, name='get_my_places'),
    path('user_places/', views.user_places, name='user_places'),
]