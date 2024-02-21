from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User as DjangoUser
from ..models import Account, User


class AccountInline(admin.TabularInline):
    model = Account.users.through
    extra = 1


class CustomUserAdmin(BaseUserAdmin):
    inlines = [AccountInline]
    list_display = ("username", "email", "accounts_list")

    def accounts_list(self, obj):
        return ", ".join([account.name for account in obj.accounts.all()])


admin.site.unregister(DjangoUser)
admin.site.register(User, CustomUserAdmin)
