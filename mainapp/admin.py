from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
admin.site.register(popularcarmodel)
admin.site.register(carstockmodel)
admin.site.register(regmodel)
admin.site.register(wishmodel)
admin.site.register(buymodel)
admin.site.register(addamount)
# Register your models here.

admin.site.register(contactmodel)
