from django.contrib import admin

from .models import Account, PlantedTree, Profile, Tree, User

admin.site.register(Account)
admin.site.register(PlantedTree)
admin.site.register(Profile)
admin.site.register(Tree)
admin.site.register(User)
