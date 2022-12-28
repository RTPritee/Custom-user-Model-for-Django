from django.db import models
from django.contrib.auth.models import User
# from django.utils.html import escape
from django.utils.html import mark_safe
from django.conf import settings
import os
import base64
# Create your models here.


def image_as_base64(image_file, format):
        
        if not os.path.isfile(image_file):
            return None
    
        encoded_string = ''
        with open(image_file, 'rb') as img_f:
            encoded_string = base64.b64encode(img_f.read())
        return 'data:image/%s;base64,%s' % (format, encoded_string)

class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=13, blank=True, unique=True)
    email = models.EmailField(blank=False, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    nid_no = models.CharField(max_length=17, blank=True, null=True)
    birthday = models.DateField(blank= True,null=True)
    # gender = models.CharField(blank=False,null=False,
    #     max_length=10,
    #     choices=[('male', 'Male'),
    #              ('female', 'Female'),
    #              ('other', 'Other')]
    # )
    # pic = models.ImageField( blank=True, null=True)

    cover = models.ImageField(blank =True,null=True)

    # def image_tag(self):
    #     return mark_safe('<img src="%s" width="60" height="60" />' % (self.pic.url))
    # image_tag.short_description = 'Image'


    def get_cover_base64(self):
        return image_as_base64(settings.MEDIA_ROOT + self.cover.path)

    # def show_cover(self):
    #     return mark_safe('<img src="{{ post.get_cover_base64 }}">')

    def __str__(self):
        return self.user.username