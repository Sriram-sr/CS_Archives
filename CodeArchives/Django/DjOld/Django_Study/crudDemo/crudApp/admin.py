from django.contrib import admin
from crudApp.models import Student
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    List = ['sno','sname','sclass','saddress']

admin.site.register(Student,studentAdmin)
