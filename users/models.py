from distutils.command.upload import upload
from django.db import models


from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.forms import DecimalField
from .managers import CustomUserManager
from django.db.models.signals import post_save,post_delete
from django.conf import settings
from django.dispatch import receiver

from decimal import Decimal



# from cloudinary.models import CloudinaryField

# Create your models here.

# we need four main class models; farmer, buyer, Supplier, agent
# from these four models, we will have four endpoints for an API
class User(AbstractBaseUser, PermissionsMixin):
    '''
    class user assumes multiple users of the application
    contact, location and username are relevant to all users. So we add these extra fields here
    Args: 
        first_name, last_name, username, email, contact, location, role
        roles extends the roles of the users in a many to many relationship if one user can have another role
        
    '''
    
    # these fields are tied to the user roles 
    # brought these fields in the model class becuase the roles are empty on registering a user i.e role = []
    # makes it even easier to use django Managers if need be
    # defining the choices and names for each choice inside the model class 
    # keeps all of that information with the class that uses it, and helps reference the choices ie User.FARMER
    FARMER = 1
    BUYER = 2
    AGENT = 3
    SUPPLIER = 4
    ADMIN = 5
    ROLE_CHOICES = (
        (FARMER, 'farmer'),
        (BUYER, 'buyer'),
        (SUPPLIER, 'supplier'),
        (AGENT, 'agent'),  
        (ADMIN, 'admin')              
    )
    
    USER_TYPE_DEFAULT = None
    
    first_name = models.CharField(max_length=255, null=False, default = '')
    last_name = models.CharField(max_length=255, null=False, default = '')
    username = models.CharField(max_length=255, null=False, default = '')
    email = models.EmailField(unique=False)
    contact = models.IntegerField(null=False, default = 0)
    location = models.CharField(max_length=255, null=False, default = 'place')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password  = models.CharField(max_length=255)
    confirm_password  = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
# profile model 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=False )
    last_name = models.CharField(max_length=120, blank=False)
    contact = models.BigIntegerField (null=False, default = 0)
    location = models.CharField(max_length=255, null=False, default = '')

    def __str__(self):
        return self.user.first_name 
  
# crop class
# from this class model, we will be able to come up with the price per crop in harvest
# price is the market price on harvest


class Crop(models.Model):
    '''
    defines the crops to be grown by the farmer
    helps define how buyers and farmers connect in terms of crops sold, bought and cultivated
    '''
    name = models.CharField(max_length=200, default = '')
    price = models.IntegerField(null=False)
    
    def __str__(self):      
        return str(self.name) 

# input class
class Inputs(models.Model):
    '''
    defines the inputs that will be converted to a loan
    gives the name of the input and the inputs amount
    class will be used by buyer, farmer, supplier and agent
    '''
    fertilizer_name = models.CharField(max_length=255, default = 'fertilizer')
    chemical_name = models.CharField(max_length=255, default='pesticide')
    seed_name = models.CharField(max_length=255, default='certified seed')
    fertilizer_bags = models.IntegerField(null=True)
    seed_bags = models.IntegerField(null=True)
    chemicals = models.IntegerField(null=True)
    fertilizer_price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    seed_price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    chemicals_price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    
    def __str__(self):      
        return self.fertilizer_name
    
    def total_fert_amount(self):
        amount = self.fertilizer_bags * self.fertilizer_price
        return amount 
    
    def total_chem_amount(self):
        amount = self.chemicals_price * self.chemicals
        return amount 
    
    def total_seed_amount(self):
        amount = self.seedlings_bags * self.seedlings_price
        return amount 



class Guarantor(models.Model):
    '''
    the guarantor acts as the security for the loan given to the farmer
    we will require their id only
    these details are filled in by the farmer as they apply for a loan
    '''
    name = models.CharField(max_length=255, null=False, default = '')
    contact = models.IntegerField(null=False, default = 0)
    location = models.CharField(max_length=255, null=False, default = '')
    identification_number = models.IntegerField(null=False)
    identification_card = models.ImageField(upload_to='images/')      
    
    def __str__(self):      
        return str(self.identification_number) 

# loan class
# class Loan(models.Model):
#     '''
#     defines the loan that a farmer applies for
#     '''
#     user


# farmer class
class Farmer(models.Model):
    '''
    is the primary player in the application as the solution and problem statement 
    revolves around them
    user can apply for a loan, view their revenues after harvest, see loans due and inpust they 
    will pick from the supplier
    Args:
        user_details, identification_number, mpesa_statements, identification_card, guarantor
        inputs_picked, loan_amount, production, crop, land_size, revenue, amount_payable
    '''
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    identification_number = models.IntegerField(null=False)
    mpesa_statements = models.ImageField(upload_to='images/')
    identification_card = models.ImageField(upload_to='images/')  
    guarantor = models.CharField(blank=True,max_length=255)  
    inputs_picked = models.ForeignKey(Inputs, on_delete=models.CASCADE, null=True)
    loan_amount = models.DecimalField(decimal_places=2, max_digits=20)
    production = models.IntegerField(null=True)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE,null=True)
    land_size = models.DecimalField(decimal_places=2, max_digits=20)
    revenue = models.DecimalField(decimal_places=2, max_digits=20)
    amount_payable = models.DecimalField(decimal_places=2, max_digits=20)
    slug = models.SlugField(max_length=100,  blank=True,null=True)


    def __str__(self):      
        return str(self.identification_number) 
    
    def save_farmer(self):
        self.save()
        
    def delete_farmer(self):
        self.delete()
        
    def loan_payable(self):
        amount = self.revenue - self.loan_amount
        return amount 
    
    def collected_inputs(self):
        farmer_inputs = Farmer.objects.get(inputs = self.inputs_picked)
        return farmer_inputs
    
    

class Supplier(models.Model):
    '''
    supplier provides the inputs to the farmer and is paid promptly depending on the
    inputs supplied
    should see their invoice as well as all inputs supplied
    Args:
        user_details, inputs_details, inputs_total, invoice
    '''
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    user_details = models.OneToOneField(Inputs, on_delete=models.CASCADE)
    inputs_total = models.IntegerField(null=True)
    invoice = models.DecimalField(decimal_places=2, max_digits=20,default=Decimal(0) )
    
    def __str__(self):      
        return str(self.user_details) 

class Buyer(models.Model):
    '''
    buyer partners with us and purchases farmer's production from our platform
    Args:
        user_details, crop_to_buy, bags_to_buy, invoice
    '''
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    crop_to_buy = models.CharField(max_length=255, null=False)
    bags_to_buy = models.IntegerField(null=True)

    invoice = models.DecimalField(decimal_places=2, max_digits=20, default=Decimal(0))

    #crop_to_buy = models.ForeignKey(Crop, on_delete=models.CASCADE)

    
    def __str__(self):      
        return str(self.invoice) 
        
    
    # the amount the buyer will pay based on their purchases
    def the_invoice(self):
        crop_price = Crop.objects.filter(price = Crop.price)
        amount = crop_price * self.bags_to_buy
        return amount 

