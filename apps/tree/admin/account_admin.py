from django.contrib import admin
from ..models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "active")
    actions = ["ativar_contas", "desativar_contas"]

    def ativar_contas(self, request, queryset):
        queryset.update(active=True)

    def desativar_contas(self, request, queryset):
        queryset.update(active=False)


admin.site.register(Account, AccountAdmin)
