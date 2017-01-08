from django.contrib import admin
from .models import Table, Order, Restaurant
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from restaurant.models import UserType
# Register your models here.

'''
Extended User model reference:
https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#extending-user
'''
# Define an inline admin descriptor for UserType model
# which acts a bit like a singleton
class UserTypeInline(admin.StackedInline):
    model = UserType
    can_delete = False
    verbose_name_plural = 'usertype'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserTypeInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Order)
admin.site.register(Restaurant)
