from django.db import models
from django.contrib.auth.models import  User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.

class Profile(models.Model):
    def validate_name(name):
        if len(name) < 3 or len(name) > 30:
            raise ValidationError("Maximum and minimum length of a name is 30 and 3 respectively")
    name=models.CharField(max_length=30,default='name',validators=[validate_name])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    # phonenumber = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=254)
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    profileimage=models.ImageField(default='default.jpg',upload_to='Uploads/user/profile', validators=[validate_image])

    def __str__(self):
        return f'{self.user.username} profile'

