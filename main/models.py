from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class Car_expert(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='Car_expert/')

    def __str__(self):
        return self.title


class Servis(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='Servis/')


    def __str__(self):
        return self.title


class About_us(models.Model):
    text1 =models.CharField(max_length=255)
    img = models.ImageField(upload_to='about_us/')
    text2 =models.TextField()

    def __str__(self):
        return self.text1


class Gallery(models.Model):
    img = models.ImageField(upload_to='Gallery/')



class Amazing_team(models.Model):
    name = models.CharField(max_length=255)
    jobs = models.CharField(max_length=255)
    img = models.ImageField(upload_to='Amazing_team/')

    def __str__(self):
        return self.name


class Employee(models.Model):
    bio = models.TextField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()