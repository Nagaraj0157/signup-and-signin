from django.contrib import admin
from myapp.models import login
class loginAdmin(admin.ModelAdmin):
    list_display=['name','email','password','rpassword']
admin.site.register(login,loginAdmin)

# Register your models here.
