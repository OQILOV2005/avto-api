from django.urls import path
from .views import *


urlpatterns = [
    path('get-banner/', get_banner),
    path('get-car_experts/', get_car_experts),
    path('get-service/', get_service),
    path('get-abouts/', get_service),
    path('get-gallerys/',get_gallerys),
    path('get-teams/', get_teams),
    path('get-employees/',get_employees),
    path('get-contacts/', get_contacts),
]