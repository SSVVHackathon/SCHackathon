from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, company_name, shelter_or_restaurant, address, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not company_name:
            raise ValueError("Users must have a company name")
        if not shelter_or_restaurant:
            raise ValueError("Users must be a shelter or restaurant")
        if not address:
            raise ValueError("Users must have an address")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            company_name=company_name,
            shelter_or_restaurant=shelter_or_restaurant,
            address=address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, company_name, shelter_or_restaurant, address, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            company_name=company_name,
            shelter_or_restaurant=shelter_or_restaurant,
            address=address,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    address = models.CharField(max_length=100, unique=True)
    shelter_or_restaurant = models.CharField(max_length=40)
    company_name = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name = 'last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'company_name'
    REQUIRED_FIELDS = ['email', 'address', 'shelter_or_restaurant', 'username',]

    objects = MyAccountManager()

    def __str__(self):
        return self.company_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
