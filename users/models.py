from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField
from location_field.models.plain import PlainLocationField

# Create your models here.

class Input(models.Model):
    fertilizer = models.CharField(max_length=255, blank=True)
    chemical = models.CharField(max_length=255, blank=True)
    seeds = models.CharField(max_length=255, blank=True)

    def __str__(self):      
        return str(self.fertilizer) 


class Plant(models.Model):
    name = models.CharField(max_length=100)
    img = CloudinaryField(blank=True)
    description = models.TextField(blank=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.TextField()
    inputs = models.ForeignKey(Input, on_delete=models.CASCADE)
    # info = models.ForeignKey(Info, on_delete=models.CASCADE)

    def __str__(self):      
        return str(self.name) 



class Land(models.Model):
    sizes = models.IntegerField()
    output = models.TextField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)


    def __str__(self):      
        return str(self.sizes) 


class Garanter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)
    contact = PhoneNumberField(blank=True)
    mpesa_statements = CloudinaryField(blank=True)
    id_img = CloudinaryField(blank=True)


    def __str__(self):      
        return str(self.name)  


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)
    contact = PhoneNumberField(blank=True)
    image = CloudinaryField('image', blank=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    trustee = models.ForeignKey(Garanter, on_delete=models.CASCADE)
    land = models.ForeignKey(Land,on_delete=models.CASCADE)


    def __str__(self):      
        return str(self.name) 


    def get_all():
        result = Profile.objects.all()
        return result

class ModuleSubscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=1, decimal_places=0)
    title = models.CharField(max_length=100)
    picture = CloudinaryField(blank=True)
    content = models.TextField(blank=True)


    
    def __str__(self):  

        return str(self.title) 


class Agents(models.Model):
    name = models.CharField(max_length=100)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    harvest = models.CharField(max_length=255)
    inputs = models.ForeignKey(Input, on_delete=models.CASCADE)


    def __str__(self):  
        return str(self.name) 