from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from ..models import Account, Profile, User


class AccountInline(admin.TabularInline):
    model = Account.users.through
    extra = 1


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(BaseUserAdmin):
    inlines = [AccountInline, ProfileInline]
    list_display = ("username", "email", "accounts_list")

    def accounts_list(self, obj):
        return ", ".join([account.name for account in obj.accounts.all()])


# admin.site.unregister(DjangoUser)
admin.site.register(User, CustomUserAdmin)
