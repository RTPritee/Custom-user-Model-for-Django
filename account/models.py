from django.db import models
from django.contrib.auth.models import User
from django.utils.html import escape
from django.utils.html import mark_safe
# Create your models here.




class Account(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=13, blank=True, unique=True)
    email = models.EmailField(blank=False, null=True)
    address = models.CharField(max_length=255,blank=True, null=True)
    nid_no = models.CharField(max_length=17, blank=True, null=True)
    pic = models.ImageField(blank=True, null=True)


    # birthday = models.DateField()
    # gender = models.CharField(
    #     max_length=10,
    #     choices=[('male', 'Male'),
    #              ('female', 'Female'),
    #              ('other', 'Other')]
    # )

    def __str__(self):
        return self.user.username

    # def pic(self):
    #     return mark_safe('<img src = "{self.pic.url}" witdh ="150" />' (self.pic))

# def pic_tag(self):
#     return u'<img src="/media/documents/%Y/%m/%d %s" width="150" height="150" />' % (self.pic_tag)


# pic_tag.short_description = 'picture'
# pic_tag.allow_tags = True
