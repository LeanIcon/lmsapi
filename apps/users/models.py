from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from apps.badge.models import Badge


class CustomUserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, password=None): #firstname, lastname,
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
        )
        
        if not email:
            raise ValueError('Users must have an email address')
        if not firstname:
            raise ValueError('Users must have an firstname')
        if not lastname:
            raise ValueError('Users must have an lastname')
        if not password:
            raise ValueError('Users must have a password')

        username = models.CharField(('username'), max_length=30, blank=True)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname='Admin', lastname='Admin', password=None):
        """
         Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, firstname, lastname,
                                password=password
                                )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    student_type = models.CharField(default='individual', max_length=15)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    # user_data = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_data')
    # preferred_name = models.CharField(max_length=100)
    avatar_url = models.CharField(max_length=255, null=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=50, null=True)
    profession = models.CharField(default='', null=True, max_length=50)
    profession_info = models.CharField(default='', null=True, max_length=50)

    education = models.CharField(default='', null=True, max_length=50)
    location = models.CharField(default='', max_length=60, null=True)
    state_region = models.CharField(default='', max_length=60, null=True)
    linkedIn_address = models.CharField(default='', max_length=60, null=True)
    facebook_address = models.CharField(default='', max_length=60, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
