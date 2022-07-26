from django.contrib import admin

# Register your models here.
from data.models import Group, Team

admin.site.register(Group)
admin.site.register(Team)
