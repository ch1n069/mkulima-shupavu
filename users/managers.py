from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser

class CustomUserManager(BaseUserManager):
    """
    Custom user model where the email address is the unique identifier
    and has an is_admin field to allow access to the admin app 
    """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_superuser = False
        user.is_staff = False
        user.save(using = self._db)
        return user 

    def create_superuser(self, email, password, **extra_fields):
        
        # extra_fields.setdefault('is_active', True)
        # extra_fields.setdefault("is_superuser", True)
        # if extra_fields.get("is_superuser") is not True:
        #     raise ValueError("Superuser must have is_superuser=True.")
        # return self.create_user(email, password, **extra_fields)

        user = self.create_user(email, password = password)
        user.is_superuser = True
        user.is_active = True 
        user.is_staff = True
        user.save(using = self._db)
        return user 
        

    