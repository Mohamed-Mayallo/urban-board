from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.


from .users.user import UserModel

admin.site.register(UserModel, UserAdmin)
