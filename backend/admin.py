from django.contrib import admin
from .models import *
from accounts.models import Accounts
# Register your models here.
admin.site.register(Board)
admin.site.register(Posts)
admin.site.register(Comments)
