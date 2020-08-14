from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Accounts


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_admin')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Accounts, AccountAdmin)
