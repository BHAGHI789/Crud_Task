from django.contrib import admin

# Register your models here.
from app.models import UserProfile
class UserProfilieadmin(admin.ModelAdmin):
    list_display=["id","user","name","email","bio"]
admin.site.register(UserProfile,UserProfilieadmin)