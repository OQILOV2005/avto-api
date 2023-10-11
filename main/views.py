from django.shortcuts import render,redirect
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def get_banner(request):
    banner = Banner.objects.last()
    ser = BannerSerializers(banner)
    return Response(ser.data)


@api_view(['GET'])
def get_car_experts(request):
    car_expert = Car_expert.objects.all()
    ser = Car_expertSerializers(car_expert, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_service(request):
    servis = Servis.objects.all()
    ser = ServisSerializers(servis, many=True)
    return Response(ser.data)

@api_view(['GET'])
def get_abouts(request):
    about_us = About_us.objects.all()
    ser = ServisSerializers(about_us, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_gallerys(request):
    gallery = Gallery.objects.all()
    ser = GallerySerializers(gallery, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_teams(request):
    amazing_team = Amazing_team.objects.all()
    ser = Amazing_teamSerializers(amazing_team, many=True)
    return Response(ser.data)

@api_view(['GET'])
def get_employees(request):
    employee = Employee.objects.all()
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)


@api_view(['POST'])
def get_contacts(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        new_contacts = Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )
        ser = ContactSerializers(new_contacts)
        return Response(ser.data)