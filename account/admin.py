from django.contrib import admin
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import mark_safe

# Register your models here.

from django.utils.html import format_html



class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'


class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInLine,)


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)


class CustomAccount(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.pic))
        #  return mark_safe('<img src="{}" width="{width}" height={height} />'.format(
        #     url = obj.pic.url,
        #     width=obj.pic.width,
        #     height=obj.pic.height,
        #     ))
   
    list_display = ['user', 'nid_no', 'image_tag']



# fields = ( 'pic_tag', )
# readonly_fields = ('pic_tag',)

admin.site.register(Account, CustomAccount)

