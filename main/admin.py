from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from main.models import Buyer


class BuyerInline(admin.StackedInline):
    model = Buyer
    can_delete = False
    verbose_name = 'Покупатель'
    verbose_name_plural = 'Покупатели'


class UserAdmin(BaseUserAdmin):
    inlines = (BuyerInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
