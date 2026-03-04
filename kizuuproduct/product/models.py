from django.db import models




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