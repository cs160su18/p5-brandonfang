from django.contrib import admin
from life.models import *

# Register your models here.
admin.site.register([User, ShopList, Group, Activity])