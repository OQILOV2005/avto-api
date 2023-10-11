from rest_framework import serializers
from .models import *

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class Car_expertSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car_expert
        fields = '__all__'


class ServisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servis
        fields =  '__all__'


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About_us

        fields =  '__all__'


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields =  '__all__'




class Amazing_teamSerializers(serializers.ModelSerializer):
    class Meta:
        model: Amazing_team
        fields =  '__all__'




class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model: Employee
        fields =  '__all__'



class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model: Employee
        fields =  '__all__'



class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model: Contact
        fields =  '__all__'