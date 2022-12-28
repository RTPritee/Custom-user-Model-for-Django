from django.contrib import admin
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import mark_safe
from baseapp import settings
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


class AdminSite(admin.ModelAdmin):
    # list_display=["image_tag", "title"]


    list_display = ('user','nid_no','cover')
admin.site.register(Account, AdminSite)
