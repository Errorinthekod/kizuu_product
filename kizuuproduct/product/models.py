from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    #
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'
    objects = UserManager()
    def __str__(self):
        return f"{self.email} {self.username}"


class Category(models.Model):

    class Status(models.IntegerChoices):
        INACTIVE = 0, "Inactive"
        ACTIVE = 1, "Active"

    name = models.CharField('Name', max_length=255, unique=True)
    slug = models.CharField('Slug', max_length=255, unique=True, null=True, blank=True )
    description = models.TextField('Description', max_length=500, null=True, blank=True)
    poster = models.ImageField('Poster', null=True, blank=True, upload_to="media/categories/")
    status = models.BooleanField('Active', choices = Status.choices, default = Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'




class Product(models.Model):

    class Status(models.IntegerChoices):
        INACTIVE = 0, "Inactive"
        ACTIVE = 1, "Active"

    name = models.CharField('Name', max_length=255, null=False, blank=False)
    slug = models.SlugField('Slug', max_length=255, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField('Description', null=True, blank=True)
    price = models.DecimalField('Price',max_digits=12, decimal_places=2, null=True, blank=True)
    poster = models.ImageField('Poster',null=True, blank=True, upload_to = 'media/posters/')
    image = models.ImageField('Image', null=True, blank=True, upload_to = 'media/images/')
    weight = models.DecimalField('Weight', max_digits=6, decimal_places=2, null=True, blank=True)
    status = models.BooleanField('Active', choices= Status.choices,  default=Status.ACTIVE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'