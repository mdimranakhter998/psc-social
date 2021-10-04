from django.contrib import admin
from .models import Contact,SignUp
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','message']


# signup models register
@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email']