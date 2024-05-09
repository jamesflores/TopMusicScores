from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import IntegrityError, models
from django.utils.text import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'


class SheetMusic(models.Model):
    rank = models.FloatField()
    item_url = models.URLField()
    cover_url = models.URLField()
    title = models.CharField(max_length=255)
    title_slug = models.SlugField(max_length=255, blank=True, null=True)
    artist = models.CharField(max_length=255)
    instruments = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    lead_time = models.CharField(max_length=255)
    list_price = models.DecimalField(max_digits=6, decimal_places=2)
    publisher = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    item_type = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.artist} ({self.instruments}) | {self.publisher} | ${self.list_price}'
