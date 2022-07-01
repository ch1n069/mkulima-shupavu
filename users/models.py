from pickle import FALSE
from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField

# Create your models here.

# we need four main class models; farmer, buyer, Supplier, agent
# from these four models, we will have four endpoints for an API

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
        return str(self.name, self.price) 

# input class
class Inputs(models.Model):
    '''
    defines the inputs that will be converted to a loan
    gives the name of the input and the inputs amount
    class will be used by buyer, farmer, supplier and agent
    '''
    fertilizer_name = models.CharField(max_length=255, default = 'fertilizer')
    chemical_name = models.CharField(max_length=255, default='pesticide')
    seedlings_name = models.CharField(max_length=255, default='certified seed')
    fertilizer_bags = models.IntegerField(null=True)
    seedlings_bags = models.IntegerField(null=True)
    chemicals = models.IntegerField(null=True)
    
    def __str__(self):      
        return str(self.fertilizer_name, self.chemical_name, self.seedlings_name) 

# profile class
class UserDetails(models.Model):
    '''
    this class represents the repetitive details of different users
    can be used in a form or profile
    these details are constant
    '''
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=255, null=False)
        
    
    def __str__(self):      
        return str(self.name) 

# guarantor class
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
    username = models.CharField(max_length=255, null=False, default = '')
    contact = models.IntegerField(null=False, default = 0)
    location = models.CharField(max_length=255, null=False, default = 'place')
    identification_number = models.IntegerField(null=False)
    mpesa_statements = models.ImageField(upload_to='images/')
    identification_card = models.ImageField(upload_to='images/')  
    # guarantor = models.OneToOneField(Guarantor, on_delete=models.CASCADE, null=True)  
    # inputs_picked = models.ForeignKey(Inputs, on_delete=models.CASCADE, null=True)
    loan_amount = models.DecimalField(decimal_places=2, max_digits=20)
    production = models.IntegerField(null=True)
    # crop = models.ForeignKey(Crop, on_delete=models.CASCADE,null=True)
    land_size = models.DecimalField(decimal_places=2, max_digits=20)
    revenue = models.DecimalField(decimal_places=2, max_digits=20)
    amount_payable = models.DecimalField(decimal_places=2, max_digits=20)
    
    def __str__(self):      
        return str(self.identification_number) 
    
class Supplier(models.Model):
    '''
    supplier provides the inputs to the farmer and is paid promptly depending on the
    inputs supplied
    should see their invoice as well as all inputs supplied
    Args:
        user_details, inputs_details, inputs_total, invoice
    '''
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=False, default = '')
    contact = models.IntegerField(null=False, default = 0)
    location = models.CharField(max_length=255, null=False, default = '')
    inputs_details = models.ForeignKey(Inputs, on_delete=models.CASCADE)
    inputs_total = models.IntegerField(null=True)
    invoice = models.DecimalField(decimal_places=2, max_digits=20)
    
    def __str__(self):      
        return str(self.invoice) 

class Buyer(models.Model):
    '''
    buyer partners with us and purchases farmer's production from our platform
    Args:
        user_details, crop_to_buy, bags_to_buy, invoice
    '''
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=False, default = '')
    contact = models.IntegerField(null=False, default = 0)
    location = models.CharField(max_length=255, null=False, default = '')
    crop_to_buy = models.CharField(max_length=255, null=False)
    bags_to_buy = models.IntegerField(null=True)
    invoice = models.DecimalField(decimal_places=2, max_digits=20)
    
    def __str__(self):      
        return str(self.invoice) 

class Agent(models.Model):
    '''
    agent is the agricultural extension officer who trains farmers in their location
    as well as keeps an inventory of produce from farmers and inputs supplied by suppliers
    within their location
    Args:
        user_details, farmer_supervising, farmers_allocated, inputs_record
    '''
    user_details = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=False, default = '')
    contact = models.IntegerField(null=False, default = 0)
    location = models.CharField(max_length=255, null=False, default = '')
    farmer_supervising = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farmers_allocated = models.IntegerField(null=True)
    inputs_record = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # harvest_record = models.ForeignKey()
    
    def __str__(self):
        return str(self.farmers_allocated)
    
    
    
    

# class Input(models.Model):
#     fertilizer = models.CharField(max_length=255, blank=True)
#     chemical = models.CharField(max_length=255, blank=True)
#     seeds = models.CharField(max_length=255, blank=True)

#     def __str__(self):      
#         return str(self.fertilizer) 


# class Plant(models.Model):
#     name = models.CharField(max_length=100)
#     img = CloudinaryField(blank=True)
#     description = models.TextField(blank=True)
#     user =  models.ForeignKey(User, on_delete=models.CASCADE)
#     price = models.TextField()
#     inputs = models.ForeignKey(Input, on_delete=models.CASCADE)
#     # info = models.ForeignKey(Info, on_delete=models.CASCADE)

#     def __str__(self):      
#         return str(self.name) 



# class Land(models.Model):
#     sizes = models.IntegerField()
#     output = models.TextField()
#     plant = models.ForeignKey(Plant, on_delete=models.CASCADE)


#     def __str__(self):      
#         return str(self.sizes) 


# class Garanter(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=255, blank=True)
#     contact = PhoneNumberField(blank=True)
#     mpesa_statements = CloudinaryField(blank=True)
#     id_img = CloudinaryField(blank=True)


#     def __str__(self):      
#         return str(self.name)  


# class Profile(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=255, blank=True)
#     contact = PhoneNumberField(blank=True)
#     image = CloudinaryField('image', blank=True)
#     user =  models.ForeignKey(User, on_delete=models.CASCADE)
#     trustee = models.ForeignKey(Garanter, on_delete=models.CASCADE)
#     land = models.ForeignKey(Land,on_delete=models.CASCADE)


#     def __str__(self):      
#         return str(self.name) 


#     def get_all():
#         result = Profile.objects.all()
#         return result

# class ModuleSubscribe(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=1, decimal_places=0)
#     title = models.CharField(max_length=100)
#     picture = CloudinaryField(blank=True)
#     content = models.TextField(blank=True)


    
#     def __str__(self):  

#         return str(self.title) 


# class Agents(models.Model):
#     name = models.CharField(max_length=100)
#     location = PlainLocationField(based_fields=['city'], zoom=7)
#     harvest = models.CharField(max_length=255)
#     inputs = models.ForeignKey(Input, on_delete=models.CASCADE)


#     def __str__(self):  
#         return str(self.name) 